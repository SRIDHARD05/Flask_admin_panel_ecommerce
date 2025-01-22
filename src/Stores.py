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
import json
from flask import jsonify
from bs4 import BeautifulSoup
from collections import Counter
import json
import re

# TODO: For Bypassing the SSL Certifications Issue's
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

db = Database.get_connection()

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
            'last_12_months': self.last_12_months,
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

    def best_seller_products(self,html_content):
        def clean_text(text):
            text = re.sub(r'\s{4,}', '   ', text)
            text = re.sub(r'\n{4,}', '\n\n\n', text)
            return text.strip()

        def format_title(title):
            return re.sub(r'\s+', ' ', title)  

        soup = BeautifulSoup(html_content, 'html.parser')
        class_combinations = []
        id_combinations = []
        class_dict = {}

        for element in soup.find_all(True):
            if element.get('class'):
                class_combination = ' '.join(element.get('class'))
                class_combinations.append(class_combination)
            if element.get('id'):
                id_combinations.append(element.get('id'))

        class_combination_counter = Counter(class_combinations)
        id_combination_counter = Counter(id_combinations)

        repeated_class_combinations = {combination: count for combination, count in class_combination_counter.items() if count > 1}
        # print(repeated_class_combinations,'\n')
        unique_repeated_class_combinations = {k: v for k, v in repeated_class_combinations.items()}
        filtered_classes_with_product = {k: v for k, v in unique_repeated_class_combinations.items() if 'product' in k}
        max_classes_with_product = Counter(filtered_classes_with_product).most_common(2)
        # print(max_classes_with_product)
        if not max_classes_with_product:
            return {"error": "No class combinations with 'product' found."}

        parent_class = max_classes_with_product[0][0]
        parent_elements = soup.find_all(class_=parent_class)

        for idx, element in enumerate(parent_elements):
            title_element = element.find('h2')
            href = element.find('a', href=True)
            all_text = element.get_text(separator="|||")

            assets = [img['src'] for img in element.find_all('img', src=True)]
            

            text_elements = [clean_text(t) for t in all_text.split("|||") if t.strip()]

            max_length_text = max(text_elements, key=len) if text_elements else ""
            title = clean_text(title_element.get_text()) if title_element else ""
            if title != max_length_text:
                title = max_length_text

            class_dict[idx] = {
                "title": title,
                "href": href['href'] if href else "",
                "assets": assets
            }
        return class_dict


class Stores:
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
    def get_store_data(store_url):
        collection = db.shopify_stores
        store_data = collection.find_one({'store_url': store_url})
        
        if store_data:
            store_data['_id'] = str(store_data['_id'])  
            # print(store_data, '\n')
            return store_data  
        else:
            return {'status': 404, 'message': 'Store not found'}  

    @staticmethod
    def view_insights(store_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        
        try:
            response = requests.get(store_url, headers=headers, verify=False)
            response.raise_for_status()
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            data_application_scripts = [script.get('data-application') for script in soup.find_all('script', attrs={'data-application': True}) if script.get('data-application')]
            data_render_region = [script.get('data-render-region') for script in soup.find_all('script', attrs={'data-render-region': True}) if script.get('data-render-region')]

            title_tag = soup.find('title')
            title = title_tag.string.strip() if title_tag else None

            meta_description_tag = soup.find('meta', attrs={'name': 'description'})
            description = meta_description_tag['content'] if meta_description_tag else None

            shop_url = None
            locale = None
            currency = None
            country = None
            theme = None
            shop_id = None
            shop_script = soup.find_all('script', string=lambda text: text and re.search(
                r'Shopify\.shop|Shopify\.locale|Shopify\.currency|Shopify\.country|Shopify\.theme', text
            ))

            for script in shop_script:
                script_content = script.string

                if 'Shopify.shop' in script_content:
                    shop_url_match = re.search(r'Shopify\.shop\s*=\s*["\'](.*?)["\'];', script_content)
                    shop_url = shop_url_match.group(1) if shop_url_match else shop_url

                if 'Shopify.locale' in script_content:
                    locale_match = re.search(r'Shopify\.locale\s*=\s*["\'](.*?)["\'];', script_content)
                    locale = locale_match.group(1) if locale_match else locale

                if 'Shopify.currency' in script_content:
                    currency_match = re.search(r'Shopify\.currency\s*=\s*{.*?"active":\s*"(.*?)".*?}', script_content)
                    currency = currency_match.group(1) if currency_match else currency

                if 'Shopify.country' in script_content:
                    country_match = re.search(r'Shopify\.country\s*=\s*["\'](.*?)["\'];', script_content)
                    country = country_match.group(1) if country_match else country

                if 'Shopify.theme' in script_content:
                    theme_match = re.search(r'Shopify\.theme\s*=\s*(.*?);', script_content)
                    theme = theme_match.group(1) if theme_match else theme

            shop_id_tag = soup.find('script', string=lambda text: text and re.search(r'window\.BOOMR\.shop_id|shop_id[=:]\s*(\d+)', text))
            if shop_id_tag:
                match = re.search(r'window\.BOOMR\.shop_id\s*=\s*"(\d+)";|shop_id[=:]\s*(\d+)', shop_id_tag.string)
                if match:
                    shop_id = match.group(1) or match.group(2)

            products_url = f'{store_url}/products.json'
            response = requests.get(products_url, headers=headers, verify=False)
            response.raise_for_status()  
            product_data = response.json()
            # json_result = json.dumps(product_data, indent=4)
            # with open("products_data.json", "w") as json_file:
            #     json_file.write(json_result)

            reports = Reports(product_data)
            data = reports.get_data()
            
            store_data = Stores.get_store_data(store_url)
            # print(store_data)

            seller_response = requests.get(f"{store_url}/collections/all?sort_by=best-selling", headers=headers, verify=False)
            seller_response.raise_for_status()
            seller_html_content = seller_response.text
            best_seller_products = reports.best_seller_products(seller_html_content)

            data.update({
                "data_application": data_application_scripts,
                "data_render_region": data_render_region,
                "title": title,
                "description": description,
                "shop_url": shop_url,
                "locale": locale,
                "currency": currency,
                "country": country,
                "theme": theme,
                "shop_id": shop_id,
                "store_title": store_data["store_url"],
                "monthly_sales": store_data["montly_sales"],
                "monthly_visits": store_data["montly_visits"],
                "social_links": store_data["social_links"],
                "total_fb_ads": store_data["total_fb_ads"],
                "total_products": store_data["total_products"],
                "best_seller_products" : best_seller_products
            })

            return data

        except requests.exceptions.RequestException as e:
            return {"error": f"Error fetching data: {str(e)}"}

        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}




