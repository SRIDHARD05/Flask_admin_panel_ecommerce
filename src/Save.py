import pymongo
from src.Database import Database
from time import time
from src import get_config
from random import randint
import bcrypt
from src.Session import Session
from mongogettersetter import MongoGetterSetter
from flask import Blueprint, render_template, redirect, url_for, request, session
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
            return {"success": False, "message": "Product not found in collection"}

        db.save.update_one(
            {"email": email},
            {"$set": {"saved_posts": user_data["saved_posts"]}}
        )

        return {"success": True, "message": "Product updated successfully in collection"}



    @staticmethod
    def create_collections(email, collection_name):
        user_data = db.save.find_one({"email": email})

        if user_data is None:
            default_data = {
                "email": email,
                "saved_posts": {
                    "saved_collections": [],
                    collection_name: []
                }
            }
            db.save.insert_one(default_data)
            return {"success": True, "message": f"User not found. Default 'saved_collections' and '{collection_name}' created."}

        if "saved_posts" not in user_data or not user_data["saved_posts"]:
            user_data["saved_posts"] = {}

        if collection_name in user_data["saved_posts"]:
            return {"success": False, "message": "Collection already exists"}

        user_data["saved_posts"][collection_name] = []

        db.save.update_one(
            {"email": email},
            {"$set": {"saved_posts": user_data["saved_posts"]}}
        )

        return {"success": True, "message": f"Collection '{collection_name}' created successfully"}


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





"""
{
  "_id": ObjectId("64efb8c3e9a2f54f4d44c91e"),
  "user_id": "user_12345",
  "username": "john_doe",
  "email" : "email"
  "saved_posts": {
    "collection_1": [
      {
        "post_id": "post_1",
        "post_title": "Post Title 1",
        "post_content": "This is the content of post 1",
        "created_at": ISODate("2025-01-01T10:00:00Z")
      },
      {
        "post_id": "post_2",
        "post_title": "Post Title 2",
        "post_content": "This is the content of post 2",
        "created_at": ISODate("2025-01-02T10:00:00Z")
      }
    ],
    "collection_2": [
      {
        "post_id": "post_3",
        "post_title": "Post Title 3",
        "post_content": "This is the content of post 3",
        "created_at": ISODate("2025-01-03T10:00:00Z")
      }
    ]
  }
}

"""