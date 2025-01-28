from src.Database import Database
from datetime import datetime
import json

db = Database.get_connection()

class Ads_data:
    @staticmethod
    def store_facebook_ads(email, collection_name, data):
        try:
            collection = db.facebook_ads

            # Prepare the document to store
            ad_data = {
                "email": email,
                "collection_name": collection_name,
                "ads_data": data.get('ads_data', []),  # Extract ad data from the JSON
                "created_at": datetime.utcnow()
            }

            # Check for duplicates (based on email and collection_name)
            existing = collection.find_one({"email": email, "collection_name": collection_name})
            if existing:
                return {
                    "success": False,
                    "message": f"Data for collection '{collection_name}' already exists."
                }

            # Insert the document into the database
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
