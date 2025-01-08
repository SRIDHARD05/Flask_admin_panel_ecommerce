import json
import hashlib
from datetime import datetime, timedelta
import logging
from datetime import datetime
import hmac
import hashlib

def get_config(key):
    config_file = "D:/GITHUB/python_flask/config.json"
    file = open(config_file, "r")
    config = json.loads(file.read())
    file.close()
    
    if key in config:
        return config[key]
    else:
        raise Exception("Key {} is not found in config.json".format(key))
    

SECRET_KEY = get_config('products_secret_key').encode()

def hash_data(id):
    return hmac.new(SECRET_KEY, id.encode(), hashlib.sha256).hexdigest()


import logging
from pymongo import MongoClient
from logging import Handler
import os


# client = MongoClient("mongodb://localhost:27017")  
# db = client.get_database('app_logs')  
# log_collection = db.logs  

# class MongoDBHandler(Handler):
#     def emit(self, record):
#         log_entry = self.format(record)
#         log_collection.insert_one({"log": log_entry})


# logging.basicConfig(
#     filename='App_logging.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
# )


# mongo_handler = MongoDBHandler()
# mongo_handler.setLevel(logging.INFO)
# mongo_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# logging.getLogger().addHandler(mongo_handler)

# def logger(admin_user, action, details=""):
#     log_message = f"Admin: {admin_user}, Action: {action}, Details: {details}"
    
#     logging.info(log_message)

#     logging.debug('debug message')
#     logging.info('info message')
#     logging.warning('warn message')
#     logging.error('error message')
#     logging.critical('critical message')

# logger("admin_user1", "Logged in", "User logged into the system")

   

