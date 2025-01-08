# import requests

# url = "https://fashor.com/collections/baarati-squad"


# response = requests.get(url)

# if response.status_code == 200:
#     content = response.text

#     with open("response_content.html", "w", encoding="utf-8") as file:
#         file.write(content)
#     print("Response content has been written to 'response_content.html'")
# else:
#     print(f"Request failed with status code: {response.status_code}")


from pymongo import MongoClient
from mongogettersetter import MongoGetterSetter
from src.Database import Database
from src.Group import Group
from src.User import User

print(User.register('username', 'password', 'password', 'name', 'email'))