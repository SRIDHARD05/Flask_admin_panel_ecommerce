from datetime import datetime
from src.Database import Database

db = Database.get_connection()

class Ads_data:
    @staticmethod
    def store_facebook_ads(email, collection_name, data):
        try:
            collection = db.facebook_ads

            ad_data = {
                "email": email,
                "collection_name": collection_name,
                "ads_data": data.get('ads_data', []), 
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }

            if not isinstance(ad_data["ads_data"], list):
                return {
                    "success": False,
                    "message": "Invalid ads_data format. It should be a list of ad details."
                }

            existing = collection.find_one({"email": email, "collection_name": collection_name})
            if existing:
                return {
                    "success": False,
                    "message": f"Data for collection '{collection_name}' already exists."
                }

            collection.insert_one(ad_data)

            return {
                "success": True,
                "message": f"Data for collection '{collection_name}' has been successfully stored."
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    
    @staticmethod
    def bulk_facebook_ads(data):
        try:
            collection = db.facebook_ads
            result_id = []  

            for ad in data:
                if not ad.get('ad_id') or not ad.get('ad_name') or not ad.get('campaign') or not ad.get('ad_set'):
                    return {"status": "error", "message": "One or more ads are missing required fields."}

                ad_data = {
                    "ad_id": ad['ad_id'],
                    "ad_name": ad['ad_name'],
                    "campaign": ad['campaign'],
                    "ad_set": ad['ad_set'],
                    "cta": ad.get('cta'),
                    "destination_url": ad.get('destination_url'),
                    "budget": ad.get('budget', 0),
                    "daily_spend": ad.get('daily_spend', 0),
                    "platforms": ad.get('platforms', []),
                    "ad_status": ad.get('ad_status', 'Active'),
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                }
                result = collection.insert_one(ad_data)
                result_id.append(str(result.inserted_id)) 
                
            return {"status": "success", "message": "Ads uploaded successfully.", "result_id": result_id}

        except Exception as e:
            return {"status": "error", "message": str(e)}

