from pymongo import MongoClient
from mongogettersetter import MongoGetterSetter
from src.LightHouseReport import LightHouseReport
# Connect to the MongoDB database and collection

# client = MongoClient("mongodb+srv://sridhardcse:sridhar@cluster0.59wpv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db = client["sample_mflix"]
# collection = db["movies"]



import json

# Load the JSON file
with open('LighthouseReport_2024-12-25.report.json', encoding='utf-8') as file:
    data = json.load(file)

# Instantiate LightHouseReport
lhr = LightHouseReport(data)

# Access the `is_https` property
print(lhr.is_https)
