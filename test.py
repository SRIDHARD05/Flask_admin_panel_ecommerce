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







from src import hash_data

print(hash_data('sdfghj'))
# from src.Save import Save
# from flask import session

# # print(Save.get_saved_posts_collections('sri@gmail.com'))
# # print(Save.create_collections('sri@gmail.com', 'collection_name'))
# # print(Save.get_saved_posts_collections('sri@gmail.com'))


# from src.Credits import Credits


# # # Store credits for a user, this will create or update the user's credits
# # response = Credits.store(email="user@example.com", credits=100)
# # print(response)


# response = Credits.create(email="newuser@example.com", credits=200)
# print(response)

# # Update credits for an existing user
# response = Credits.update(email="user@example.com", credits=+1000)
# print(response)



""""

# def find_repeated_class_and_id_combinations(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     class_combinations = []
#     id_combinations = []

#     for element in soup.find_all(True):  
#         if element.get('class'):
#             class_combination = ' '.join(element.get('class')) 
#             class_combinations.append(class_combination)
#         if element.get('id'):
#             id_combinations.append(element.get('id'))  

#     class_combination_counter = Counter(class_combinations)
#     id_combination_counter = Counter(id_combinations)

#     repeated_class_combinations = {combination: count for combination, count in class_combination_counter.items() if count > 1}
#     repeated_id_combinations = {combination: count for combination, count in id_combination_counter.items() if count > 1}

#     return repeated_class_combinations, repeated_id_combinations

# repeated_class_combinations, repeated_id_combinations = find_repeated_class_and_id_combinations(html_content)
# unique_repeated_class_combinations = {k: v for k, v in repeated_class_combinations.items()}
# filtered_classes_with_product = {k: v for k, v in unique_repeated_class_combinations.items() if 'product' in k}
# max_classes_with_product = Counter(filtered_classes_with_product).most_common(2)

# def extract_data(html_content, parent_class):
#     def clean_text(text):
#         text = re.sub(r'\s{4,}', '   ', text)
#         text = re.sub(r'\n{4,}', '\n\n\n', text)
#         return text.strip()

#     soup = BeautifulSoup(html_content, 'html.parser')
#     class_dict = {}

#     parent_elements = soup.find_all(class_=parent_class)

#     for idx, element in enumerate(parent_elements):
#         title_element = element.find('h2')
#         href = element.find('a', href=True)
#         all_text = element.get_text(separator="|||")

#         assets = [img['src'] for img in element.find_all('img', src=True)]
#         assets_string = ', '.join(assets)

#         text_elements = [clean_text(t) for t in all_text.split("|||") if t.strip()]

#         max_length_text = max(text_elements, key=len) if text_elements else ""
#         max_length = len(max_length_text)

#         title = clean_text(title_element.get_text()) if title_element else ""
#         if title != max_length_text:
#             title = max_length_text

#         class_dict[idx] = {
#             "title": title,
#             "href": href['href'] if href else "",
#             "assets": assets_string,
#             "max_length": max_length
#         }
#     return class_dict
# result = extract_data(html_content, max_classes_with_product[0][0])




""""