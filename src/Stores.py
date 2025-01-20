from src.Database import Database
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import UpdateOne
from bson import ObjectId
import requests
import re
import urllib3  
from datetime import datetime, timedelta
import pytz

class Reports:
    def __init__(self, data):
        self.products = data['products']
        self.total_products = 0
        self.vendor = {}
        self.tags = {}
        self.total_price = 0
        self.max_price = float('-inf')
        self.min_price = float('inf')
        self.first_modified = None
        self.last_modified = None
        self.last_6_months = {}
        self.last_12_months = {}
        self.product_types = {}
        self.keywords = set()
        self.get_data()

    def get_data(self):
        current_date = datetime.now(pytz.utc)

        for product in self.products:
            self.total_products += 1
            vendor_name = self.extract_vendor_name(product)
            self.update_vendor_data(vendor_name)

            self.update_tags_data(product.get('tags', []))
            self.update_product_types_data(product)

            self.update_price_data(product.get('variants', []))

            created_date = product.get("created_at")
            self.update_modified_dates(created_date, product.get("updated_at"))

            created_datetime = self.parse_datetime(created_date)
            self.update_monthly_launches(created_datetime, current_date)

            self.extract_keywords(product)

        avg_price = self.total_price / self.total_products if self.total_products > 0 else 0
        
        return {
            'vendors': self.vendor,
            'tags': self.tags,
            'product_types': self.product_types,
            'keywords': list(self.keywords),
            'total_products': self.total_products,
            'total_price': self.total_price,
            'average_price': avg_price,
            'max_price': self.max_price,
            'min_price': self.min_price,
            'first_modified': self.first_modified,
            'last_modified': self.last_modified,
            'last_6_months': self.last_6_months,
            'last_12_months': self.last_12_months
        }

    def extract_vendor_name(self, product):
        return product.get("vendor", "Unknown Vendor")
    
    def update_vendor_data(self, vendor_name):
        if vendor_name in self.vendor:
            self.vendor[vendor_name] += 1
        else:
            self.vendor[vendor_name] = 1

    def update_tags_data(self, tags):
        for tag in tags:
            if tag in self.tags:
                self.tags[tag] += 1
            else:
                self.tags[tag] = 1

    def update_product_types_data(self, product):
        product_type = product.get("type", "None")  
        if product_type == "": 
            return
        if product_type in self.product_types:
            self.product_types[product_type] += 1
        else:
            self.product_types[product_type] = 1

    def update_price_data(self, variants):
        for variant in variants:
            price = float(variant.get('price', 0))
            self.total_price += price
            self.max_price = max(self.max_price, price)
            self.min_price = min(self.min_price, price)

    def update_modified_dates(self, created_date, modified_date):
        if created_date and (self.first_modified is None or created_date < self.first_modified):
            self.first_modified = created_date
        
        if modified_date and (self.last_modified is None or modified_date > self.last_modified):
            self.last_modified = modified_date

    def update_monthly_launches(self, created_datetime, current_date):
        if current_date - created_datetime <= timedelta(days=180): 
            month_year = created_datetime.strftime("%Y-%m")
            self.last_6_months[month_year] = self.last_6_months.get(month_year, 0) + 1

        if current_date - created_datetime <= timedelta(days=365):  
            month_year = created_datetime.strftime("%Y-%m")
            self.last_12_months[month_year] = self.last_12_months.get(month_year, 0) + 1

    def parse_datetime(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")  
        except ValueError:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")  

    def extract_keywords(self, product):
        title = product.get("title", "")
        title = re.sub(r'[^a-zA-Z\s]', '', title)
        title = re.sub(r'\s+', ' ', title)
        title = re.sub(r'\d+', '', title)
        title = re.sub(r'\(.*?\)', '', title)
        title = title.strip()

        if title:
            self.keywords.add(title)


# TODO: For Bypassing the SSL Certifications Issue's
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

db = Database.get_connection()

class Stores:
    def __init__(self):
        self.reports = Reports()

    @staticmethod
    def store_save(html_content):
        collection = db.shopify_stores
        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all('tr', class_='el-table__row')
        data_to_save = []

        for row in rows:
            try:
                index = row.find('td', class_='el-table_1_column_1').find('div', class_='table_shown_fr').text.strip()
                name = row.find('td', class_='el-table_1_column_2').find('p', class_='tableTitle').text.strip()
                categories = [
                    category.text.strip()
                    for category in row.find('td', class_='el-table_1_column_2').find_all('span', class_='categoryLabel')
                ]
                website = row.find('td', class_='el-table_1_column_2').find('a', class_='tableTipLink')['href']
                views = row.find('td', class_='el-table_1_column_3').find('span').text.strip()
                revenue = row.find('td', class_='el-table_1_column_4').text.strip()
                followers = row.find('td', class_='el-table_1_column_5').find('span').text.strip()

                social_links_elements = row.find('td', class_='el-table_1_column_6').find_all('a', href=True)
                social_links = {}
                for link in social_links_elements:
                    href = link['href']
                    if 'facebook.com' in href:
                        social_links['facebook_url'] = href
                    elif 'instagram.com' in href:
                        social_links['instagram_url'] = href
                    elif 'twitter.com' in href:
                        social_links['twitter_url'] = href
                    elif 'youtube.com' in href:
                        social_links['youtube_url'] = href
                    elif 'pinterest.com' in href:
                        social_links['pinterest_url'] = href
                    elif 'snapchat.com' in href:
                        social_links['snapchat_url'] = href
                    

                total_fb_ads = row.find('td', class_='el-table_1_column_7').find('div', class_='table_shown_th_other').text.strip()
                store_data = {
                    'store_title': name,
                    'store_categories': categories,
                    'store_url': website,
                    'total_products': views,
                    'montly_visits': revenue,
                    'montly_sales': followers,
                    'social_links': social_links,
                    'timestamp': datetime.utcnow(),
                    'total_fb_ads': total_fb_ads
                }

                data_to_save.append(UpdateOne({'store_url': website}, {'$set': store_data}, upsert=True))
            except Exception as e:
                print(f"Error processing row: {e}")

        if data_to_save:
            try:
                collection.bulk_write(data_to_save)
                return {'message': 'Data saved successfully', 'status': 200}
            except Exception as e:
                print(f"Error saving to database: {e}")
                return {'message': 'Error saving to database', 'status': '500'}
        else:
            return {'message': 'No data to update', 'status': '204'}

    @staticmethod
    def store_view():
        collection = db.shopify_stores
        try:
            stores = collection.find()

            store_list = [
                {
                    "store_title": store.get("store_title", "N/A"),
                    "store_categories": store.get("store_categories", []),
                    "store_url": store.get("store_url", "N/A"),
                    "total_products": store.get("total_products", 0),
                    "monthly_visits": store.get("montly_visits", "N/A"),
                    "monthly_sales": store.get("montly_sales", "N/A"),
                    "social_links": store.get("social_links", {}),
                    "timestamp": store.get("timestamp"),
                    "total_fb_ads": store.get("total_fb_ads", "N/A")
                }
                for store in stores
            ]

            return {"data": store_list, "message": "Data retrieved successfully", "status": 200}

        except Exception as e:
            print(f"Error retrieving data: {str(e)}")
            return {"message": f"Error occurred: {str(e)}", "status": "500"}

    @staticmethod
    def best_stores_save(store_type, username, html_content):
        STORE_COLLECTIONS = {
            'aliexpress': db.aliexpress,
            'amazon': db.amazon_store,
            'lazada': db.lazada_store,
            'shope': db.shope_store,
            'shopify': db.shopify_store,
            'wish': db.wish_store,
            'austrilia': db.austrilia_store,
            'brazil': db.brazil_store,
            'canada': db.canada_store,
            'france': db.france_store,
            'uk': db.uk_store,
            'us': db.us_store,
            'beauty': db.beauty_store,
            'clothing': db.clothing_store,
            'consumer': db.consumer_store,
            'home_improvement': db.home_improvement_store,
            'home': db.home_store,
            'office': db.office_store,
            'sports': db.sports_store,
            'toyes': db.toyes_store
        }

        collection = STORE_COLLECTIONS.get(store_type)
        if collection is None:
            return {'message': f"Invalid store type: {store_type}", 'status': '400'}

        soup = BeautifulSoup(html_content, 'html.parser')
        data_to_save = []

        try:
            for row in soup.find_all('div', class_='row-item'):
                social_media_anchors = row.find('div', class_='column-item column-item7').find_all('a') if row.find('div', class_='column-item column-item7') else []
                social_media = {key: "" for key in ["face_book_url", "instagram_url", "twitter_url", "youtube_url", "pinterest_url", "snapchat_url"]}

                for anchor in social_media_anchors:
                    platform = anchor.find('img')['alt'].lower() if anchor.find('img') else 'unknown'
                    url = anchor['href'] if anchor.has_attr('href') else 'N/A'

                    if 'facebook' in platform:
                        social_media["face_book_url"] = url
                    elif 'instagram' in platform:
                        social_media["instagram_url"] = url
                    elif 'twitter' in platform:
                        social_media["twitter_url"] = url
                    elif 'youtube' in platform:
                        social_media["youtube_url"] = url
                    elif 'pinterest' in platform:
                        social_media["pinterest_url"] = url
                    elif 'snapchat' in platform:
                        social_media["snapchat_url"] = url

                store_data = {
                    'email': username,
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'sort_order': row.find('div', class_='sort').text.strip() if row.find('div', class_='sort') else 'N/A',
                    'shop_name': row.find('div', class_='shop-name').text.strip() if row.find('div', class_='shop-name') else 'N/A',
                    'shop_url': row.find('a')['href'] if row.find('a') else 'N/A',
                    'platform': row.find('div', class_='column-item column-item3').text.strip() if row.find('div', class_='column-item column-item3') else 'N/A',
                    'category': row.find('div', class_='column-item column-item4').text.strip() if row.find('div', class_='column-item column-item4') else 'N/A',
                    'monthly_visits': row.find('div', class_='column-item column-item5').text.strip() if row.find('div', class_='column-item column-item5') else 'N/A',
                    'monthly_sales': row.find('div', class_='column-item column-item6').text.strip() if row.find('div', class_='column-item column-item6') else 'N/A',
                    'social_media': social_media
                }

                data_to_save.append(
                    UpdateOne(
                        {'shop_url': store_data['shop_url']},   
                        {'$set': store_data},  
                        upsert=True   
                    )
                )

            if data_to_save:
                collection.bulk_write(data_to_save)
                return {'message': 'Data saved successfully', 'status': '200'}
            else:
                return {'message': 'No data to update', 'status': '204'}

        except Exception as e:
            print(f"Error details: {str(e)}")
            return {'message': f'Error occurred: {str(e)}', 'status': '500'}

    @staticmethod
    def best_stores_view(store_type):
        STORE_COLLECTIONS = {
            'aliexpress': db.aliexpress,
            'amazon': db.amazon_store,
            'lazada': db.lazada_store,
            'shope': db.shope_store,
            'shopify': db.shopify_store,
            'wish': db.wish_store,
            'austrilia': db.austrilia_store,
            'brazil': db.brazil_store,
            'canada': db.canada_store,
            'france': db.france_store,
            'uk': db.uk_store,
            'us': db.us_store,
            'beauty': db.beauty_store,
            'clothing': db.clothing_store,
            'consumer': db.consumer_store,
            'home_improvement': db.home_improvement_store,
            'home': db.home_store,
            'office': db.office_store,
            'sports': db.sports_store,
            'toyes': db.toyes_store
        }

        collection = STORE_COLLECTIONS.get(store_type)
        if collection is None:
            return {'message': f"Invalid store type: {store_type}", 'status': '400'}

        try:
            data = list(collection.find())
            for item in data:
                item['sort_order'] = int(item.get('sort_order', 0))  

            data.sort(key=lambda x: x['sort_order'])  
            return data
        except Exception as e:
            return {'message': f'Error occurred: {str(e)}', 'status': '500'}


    @staticmethod
    def view_insights(store_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }

        try:
            html_content = requests.get(store_url, headers=headers, verify=False).text
            soup = BeautifulSoup(html_content, 'html.parser')

            script_tag = soup.find('script', text=re.compile(r'window\.BOOMR\.shop_id|shop_id[=:]\s*(\d+)'))
            
            if script_tag:
                match = re.search(r'window\.BOOMR\.shop_id\s*=\s*"(\d+)";|shop_id[=:]\s*(\d+)', script_tag.string)
                if match:
                    shop_id = match.group(1) or match.group(2)
                    data = {}
                    data['shop_id'] = shop_id

                    # TODO: Products Data
                    store_url = f'{store_url}/products.json'
                    product_data = requests.get(store_url, headers=headers, verify=False).text
                    reports = Reports(product_data)
                    
                    data = reports.get_data()
                    return data
                    
            return 'Error Fetching the Shop ID'

        except requests.exceptions.RequestException as e:
            return f"Error fetching data: {str(e)}"

    def parse_view_insight(html_content):
        return html_content