import pymongo
from src.Database import Database
from time import time
from src import get_config
from random import randint
import bcrypt
from mongogettersetter import MongoGetterSetter
from uuid import uuid4

db = Database.get_connection()
apps = db.shopify_apps

class Shopify:
    @staticmethod
    def get_best_apps():
        collection = db.shopify_apps
        apps = list(collection.find())   
        for app in apps:
            app['rating'] = int(app['rating'])  
        return apps


