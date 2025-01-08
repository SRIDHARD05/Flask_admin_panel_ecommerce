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
    def save_posts(user_id, media_type,product_id,product_id_hash):
        _id = saved_data.insert_one({
            "user_id" : user_id,
            "media_type" : media_type,
            "product_id" : product_id,
            "product_id_hash" : product_id_hash,
            "saved_at": time(),
        })
        return _id

    @staticmethod
    def create_collections(user_id, collection_name):
        pass
    
    @staticmethod
    def get_saved_posts_collections(email):
        saved_collections = save_posts.find_one({"email": email})
        return list(user["saved_posts"].keys())


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