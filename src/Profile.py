import pymongo
from src.Database import Database
from time import time
from src import get_config
from random import randint
import bcrypt
from src.Session import Session
from mongogettersetter import MongoGetterSetter
from uuid import uuid4
from flask import Blueprint, render_template, redirect, url_for, request, session

db = Database.get_connection()
profile_db = db.profile
users = db.users

class ProfileCollection(metaclass=MongoGetterSetter):
    def __init__(self, email):
        self._collection = db.profile
        self._filter_query = {
            "$or": [
                {"email": email}, 
                {"id": email}
            ]
        }
        
class Profile:
    def __init__(self, id):
        self.collection = ProfileCollection(id)
        self.id = self.collection.id
        self.email = self.collection.email        

    @staticmethod
    def save_user(first_name, last_name, email, location, phonenumber):
        if not email:
            return {"status": 400, "message": "Email is required"}

        existing_user = db.profile.find_one({"email": email})
        user = users.find_one({'email' : email})
        if existing_user:
            updated_profile = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "location": location,
                "phonenumber": phonenumber,
                "updated_time": time(),
                "user_id" : user['id']
            }

            profile_db.update_one({"email": email}, {"$set": updated_profile})

            return {
                "status": 200,
                "message": "Profile updated successfully"
            }

        else:
            new_profile = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "location": location,
                "phonenumber": phonenumber,
                "created_time":time(),
                "updated_time": time(),
                "user_id" : user['id']
            }

            profile_db.insert_one(new_profile)

            return {
                "status": 200,
                "message": "Profile created successfully"
            }

    @staticmethod
    def get_user_profile(email):
        return profile_db.find_one({'email' : email})

    @staticmethod
    def reset_password(email, old_password, new_password):
        if not email or not old_password or not new_password:
            return {"status": 400, "message": "Email, old password, and new password are required"}

        user = users.find_one({"email": email})
        if not user:
            return {"status": 404, "message": "User not found"}

        if not bcrypt.checkpw(old_password.encode('utf-8'), user.get('password', b"")):
            return {"status": 400, "message": "Old password does not match"}

        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        users.update_one({"email": email}, {"$set": {"password": hashed_password, "updated_time": time(),'user_id' : user.id}})

        return {"status": 200, "message": "Password reset successfully"}
