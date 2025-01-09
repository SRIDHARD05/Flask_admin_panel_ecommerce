# from pymongo import MongoClient
# from mongogettersetter import MongoGetterSetter
# from src.LightHouseReport import LightHouseReport
# # Connect to the MongoDB database and collection

# # client = MongoClient("mongodb+srv://sridhardcse:sridhar@cluster0.59wpv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# # db = client["sample_mflix"]
# # collection = db["movies"]



# import json

# with open('LighthouseReport_2024-12-25.report.json', encoding='utf-8') as file:
#     data = json.load(file)

# lhr = LightHouseReport(data)

# print(lhr.is_https)


# import logging
# from datetime import datetime


# # logging.basicConfig(
# #     filename='admin_activity.log',
# #     level=logging.INFO,
# #     format='%(asctime)s - %(levelname)s - %(message)s',
# # )

# # def log_action(admin_user, action, details=""):
# #     log_message = f"Admin: {admin_user}, Action: {action}, Details: {details}"
# #     logging.info(log_message)
# #     logging.debug('debug message')
# #     logging.info('info message')
# #     logging.warning('warn message')
# #     logging.error('error message')
# #     logging.critical('critical message')

# """
# if user:
#     session['username']
#     session['user_id']
#     session['logged_time_stamp']
#     session['roles']
#     session['language']
#     session['cart'] = {'item1': 2, 'item2': 1}.
#     session['is_available_tokens']
#     session['is_subscribed']


# from pymongo import MongoClient
# from mongogettersetter import MongoGetterSetter
# from src.Database import Database
# from src.Group import Group
# from src.User import User
# from src.Profile import Profile

# print(User.register('username', 'password', 'password', 'name', 'email'))


# print(Profile.save_user('first_name', 'last_name', 'email', 'location', 'phonenumber'))

# print(Profile.reset_password("example@user.com", 'password'))







# from src import hash_data

# print(hash_data('sdfghj'))
from src.Save import Save
from flask import session

# print(Save.get_saved_posts_collections('sri@gmail.com'))
# print(Save.create_collections('sri@gmail.com', 'collection_name'))
print(Save.get_saved_posts_collections('sri@gmail.com'))