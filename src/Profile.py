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
profile = db.profile


class Profile:
    @staticmethod
    def save_user(first_name,last_name,email,location,phonenumber):
        _id = users.insert_one({
            "updated_time": time(),
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "location" : location,
            "phonenumber" : phonenumber
        })
        return _id
