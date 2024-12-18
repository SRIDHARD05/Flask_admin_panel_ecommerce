from pymongo import MongoClient
from mongogettersetter import MongoGetterSetter

# Connect to the MongoDB database and collection

client = MongoClient("mongodb+srv://sridhardcse:sridhar@cluster0.59wpv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["sample_mflix"]
collection = db["movies"]

# Wrapper for MongoDB Collection with metaclass, use this inside your actual class.
class EmployeeCollection(metaclass=MongoGetterSetter):
    def __init__(self, _id):
        self._filter_query = {"id": _id} # or the ObjectID, at your convinence
        self._collection = collection # Should be a pymongo.MongoClient[database].collection

class Employee:
    def __init__(self, _id):
        self._filter_query = {"id": _id}
        self._collection = collection
        self.collection = EmployeeCollection(_id)

        # Create a new document if it doesn't exist
        if self.collection.get() is None:
            self._collection.insert_one(self._filter_query)
    
    def someOtherOperation(self):
        self.collection.hello = "Hello World"  


