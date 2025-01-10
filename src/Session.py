from time import time
from uuid import uuid4
import pymongo
from src.Database import Database
from mongogettersetter import MongoGetterSetter

db = Database.get_connection()
users = db.users
sessions = db.sessions

# SECRET_KEY = get_config('products_secret_key').encode()

# # Helper methods for hashing and verifying session IDs
# def sign_user_id(user_id):
#     """ Sign the user ID to prevent tampering """
#     signature = hmac.new(SECRET_KEY, user_id.encode(), hashlib.sha256).digest()
#     signed_user_id = f"{user_id}.{base64.urlsafe_b64encode(signature).decode()}"
#     return signed_user_id

# def verify_user_id(signed_user_id):
#     """ Verify the signed user ID """
#     try:
#         user_id, signature = signed_user_id.rsplit('.', 1)
#         expected_signature = base64.urlsafe_b64encode(
#             hmac.new(SECRET_KEY, user_id.encode(), hashlib.sha256).digest()
#         ).decode()
#         if hmac.compare_digest(signature, expected_signature):
#             return user_id  # Return the original user ID if valid
#         return None
#     except Exception:
#         return None

class SessionCollection(metaclass=MongoGetterSetter):
    def __init__(self, id):
        self._collection = db.sessions
        self._filter_query = {"id": id}
        
class Session:
    def __init__(self, id):
        self.id = id
        self.collection = SessionCollection(id)
        
    def is_valid(self):
        login_time = self.collection.time
        validity = self.collection.validity
        now = time()
        return now - login_time < validity
        
    @staticmethod
    def register_session(username, request=None, validity=604800, _type="plain"):
        uuid = str(uuid4())
        collection = db.sessions
        """
        If user logsout, we set active to False and delete the session
        If user logs in, we set active to True and create a new session
        If user is inactive for 7 days, we discard the session, and discard active=True since validity expired
        
        Types:
        
        1. plain - Username and Password used for authentication
        2. api - API Key used for authentication
        """
        
        if request is not None:
            request_info = {
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent'),
                'method': request.method,
                'url': request.url,
                'headers': dict(request.headers),
                'data': request.get_data().decode('utf-8')
            }
        else:
            request_info = None
        
        result = collection.insert_one({
            "id": uuid,
            "username": username,
            "time": time(),
            "validity": validity,  # 7 days
            "active": True,
            "type": _type,
            "request": request_info
        })
        
        return Session(uuid)

   