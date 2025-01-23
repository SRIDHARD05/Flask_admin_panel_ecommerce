from src.Session import Session
from src.Database import Database
from time import time
from random import randint
import bcrypt
from uuid import uuid4
from flask import Blueprint, render_template, redirect, url_for, request, session
from src.Save import Save
from mongogettersetter import MongoGetterSetter


db = Database.get_connection()
users = db.users

class UserCollection(metaclass=MongoGetterSetter):
    def __init__(self, email):
        self._collection = db.users
        self._filter_query = {
            "$or": [
                {"email": email}, 
                {"id": email}
            ]
        }
        
class User:
    def __init__(self, id):
        self.collection = UserCollection(id)
        self.id = self.collection.id
        self.email = self.collection.email        
    
    @staticmethod
    def login(email, password):
        result = users.find_one({
            "email": email
        })
        if result:
            hashedpw = result['password']
            if bcrypt.checkpw(password.encode(), hashedpw):
                sess = Session.register_session(email, request=request)
                return { 'sess_id' : sess.id,
                'role' : result['role'],
                'user_id' : result['id'],
                'credits' : result['credits'],
                'username' : result['username']
                }
            else:
                raise Exception("Incorrect Password")
        else:
            raise Exception("Incorrect Credentials")

    @staticmethod
    def register(username, password, confirm_password, email):
        uuid = str(uuid4())
        if password != confirm_password:
            raise Exception("Password and Confirm Password do not match")
        
        password = password.encode()
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(password, salt)
        # TODO: add the role to dynamically
        role = 'user'
        _id = users.insert_one({
            "username": username,
            "password": password,
            "register_time": time(),
            "active": False,
            "activate_token": randint(100000, 999999),
            "id": uuid,
            "role" : role,
            "email" : email,
            "credits" : 200  
        })
        # TODO: Do this into after user redirected to dashboard
        create_collections = Save.create_collections(email,uuid)
        return {
            'uuid' : uuid,
            'role' : role,
        }
    
    @staticmethod
    def get_user(email):
        return db.users.find_one({'email' : email})

    @staticmethod
    def log_unauthorized_attempt(user_data):
        with open("unauthorized_access.log", "a") as log_file:
            log_file.write(f"Unauthorized Developer Tools access attempt by user: {user_data.get('email', 'Unknown')}\n")
    
    @staticmethod
    def get_credits():
        if "authenticated" in session :
            email = session['email']
            user = users.find_one({"email": email})
            if user:
                return user.get("credits", 0)  
            return None 
        else:
            return redirect(url_for('signin'))

    @staticmethod
    def add_credits(new_credits): 
        if "authenticated" in session:
            email = session.get('email')
            result = users.update_one(
                {"email": email},
                {"$set": {"credits": new_credits}}
            )
            if result.modified_count > 0:
                session['credits'] = new_credits
                return True 
            return False 
        return None 

    @staticmethod
    def update_credits(credits):
        try:
            if "authenticated" in session:
                email = session.get('email')

                if not email:
                    return None 
                user = users.find_one({"email": email}, {"credits": 1})

                if not user:
                    return None 
                current_credits = int(user.get('credits', 0))
                new_credits = current_credits + int(credits)
                result = users.update_one(
                    {"email": email},
                    {"$set": {"credits": new_credits}}
                )

                if result.modified_count > 0:
                    return new_credits  
                return False 
            return None 
        except Exception as e:
            print(f"Error in update_credits: {e}")  
            raise
