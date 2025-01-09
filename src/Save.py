import pymongo
from src.Database import Database
from time import time
from src import get_config
from random import randint
import bcrypt
from src.Session import Session
from mongogettersetter import MongoGetterSetter
from uuid import uuid4

db = Database.get_connection()
saved_data = db.save


class SaveCollection(metaclass=MongoGetterSetter):
    def __init__(self, email):
        self._collection = saved_data
        self._filter_query = {
            "$or": [
                {"email": email}, 
                {"id": email}
            ]
        }
        
class Save:
    def __init__(self, id):
        self.collection = SaveCollection(id)
        self.id = self.collection.id
        self.email = self.collection.email        
    
    
    @staticmethod
    def save_posts(email, collection_name, media_type, product_id, product_id_hash):
        user_data = db.save.find_one({"email": email})
        
        if not user_data:
            raise ValueError("User not found")

        if "saved_posts" not in user_data:
            user_data["saved_posts"] = {}

        if collection_name not in user_data["saved_posts"]:
            user_data["saved_posts"][collection_name] = []

        collection = user_data["saved_posts"][collection_name]

        for product in collection:
            if product["product_id"] == product_id:
                product["saved_at"] = time() 
                break
        else:
            new_product = {
                "product_id": product_id,
                "product_id_hash": product_id_hash,
                "media_type": media_type,
                "saved_at": time()
            }
            user_data["saved_posts"][collection_name].append(new_product)

        db.save.update_one(
            {"email": email},
            {"$set": {"saved_posts": user_data["saved_posts"]}}
        )

        return {"success": True, "message": "Product saved successfully in collection"}

    @staticmethod
    def create_collections(email,user_id, collection_name):
        user_data = db.save.find_one({"email": email})

        if user_data is None:
            default_data = {
                "user_id" : user_id,
                "email": email,
                "saved_posts": {
                    collection_name: []  
                }
            }
            db.save.insert_one(default_data)
            return {"success": True, "message": f"User not found. Default data and collection '{collection_name}' created."}

        if "saved_posts" not in user_data or not user_data["saved_posts"]:
            user_data["saved_posts"] = {}

        if collection_name in user_data["saved_posts"]:
            return {"success": False, "message": f"Collection '{collection_name}' already exists."}

        user_data["saved_posts"][collection_name] = []

        db.save.update_one(
            {"email": email},
            {"$set": {"saved_posts": user_data["saved_posts"]}}
        )
        return {"success": True, "message": f"Collection '{collection_name}' created successfully."}


    @staticmethod
    def get_saved_posts_collections(email):
      saved_collections = db.save.find_one({"email": email})
      saved_posts = saved_collections['saved_posts']
      return list(saved_posts.keys())

    @staticmethod
    def get_saved_posts(email, collection_name):
        user_data = db.save.find_one({"email": email})
        
        if not user_data:
            raise ValueError("User not found")
        
        if "saved_posts" not in user_data or not user_data["saved_posts"]:
            return []

        if collection_name not in user_data["saved_posts"]:
            raise ValueError(f"Collection '{collection_name}' not found")

        return user_data["saved_posts"][collection_name]

    @staticmethod
    def delete_collection(email, collection_name):
        user_data = db.save.find_one({"email": email})
        if not user_data or "saved_posts" not in user_data:
            return {"success": False, "message": "No saved posts found for this user."}

        if collection_name not in user_data["saved_posts"]:
            return {"success": False, "message": f"Collection '{collection_name}' not found."}

        db.save.update_one(
            {"email": email},  
            {"$unset": {f"saved_posts.{collection_name}": ""}}  
        )

        return {"success": True, "message": f"Collection '{collection_name}' deleted successfully."}

    @staticmethod
    def delete_post(email, collection_name, post_name):
        try:
            
            user_data = db.save.find_one({"email": email})
            if not user_data:
                return {"status": 400, "message": "User not found."}

            if "saved_posts" not in user_data or collection_name not in user_data["saved_posts"]:
                return {"status": 400, "message": "Collection not found."}

            collection = user_data["saved_posts"][collection_name]

            post_to_delete = next((post for post in collection if post['product_id'] == post_name), None)
            if not post_to_delete:
                return {"status": 400, "message": "Post not found in collection."}

            user_data["saved_posts"][collection_name] = [
                post for post in collection if post['product_id'] != post_name
            ]

            result = db.save.update_one(
                {"email": email},
                {"$set": {"saved_posts": user_data["saved_posts"]}}
            )

            if result.modified_count > 0:
                return {"status": 200, "message": "Post deleted successfully."}
            else:
                return {"status": 400, "message": "No changes were made."}

        except Exception as e:
            print(f"Error: {str(e)}")
            return {"status": 500, "message": "An internal error occurred."}