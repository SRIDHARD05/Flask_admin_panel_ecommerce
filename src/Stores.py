from src.Database import Database
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import UpdateOne
from bson import json_util, ObjectId   

db = Database.get_connection()

class Stores:
    @staticmethod
    def save(store_type, username, html_content):
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
        data = []

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
                
                data.append(store_data)

            if data:
                insert_result = collection.insert_many(data)
                inserted_ids = [str(obj) for obj in insert_result.inserted_ids]  
                return {'message': 'Data saved successfully', 'status': '200'}
            else:
                return {'message': 'No data to update', 'status': '204'}

        except Exception as e:
            print(f"Error details: {str(e)}")
            return {'message': f'Error occurred: {str(e)}', 'status': '500'}

    @staticmethod
    def view(store_type):
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


