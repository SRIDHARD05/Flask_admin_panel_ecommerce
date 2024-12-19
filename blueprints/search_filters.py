from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("search_filters", __name__, url_prefix="/search_filters")


@bp.route('load_data', methods=['POST'])  
def load_data():
   data = request.get_json() 
   starting_id = data.get("starting_id", "")
   ending_id = data.get("ending_id", "")

   '''
   # TODO:  Fetch the Datas from the database
   # load_data = Load_data().load_data(starting_id,ending_id)
   
   # TODO: Fetch the templates and append the databases from the db to templates
   # TODO: Implement encode the PRoduct UUID to Avaoid the UUID Hijacking
   # TODO: Like Add the Tabs Name to UUID -> tab-name-uuid -> facebook-15b75572-bec9-4a1a-9d35-5d587b00f2a4
   # TODO: Encode the UUID with Tab Name -> get the integers length and remove the "-" and append the all strings into single string and add the tab name

   '''
   
   datas = [
      {
         "title": "Today's Money 1",
         "value": "$12k",
         "icon": "weekend",
         "change_class": "success",
         "change": "+12%",
         "description": "than last week",
         "product_uuid": "f91e4c65-2d45-45d1-bf6c-c89cbb9579f4",
         "category_1_title": "Category A",
         "category_2_title": "Category X",
         "category_3_title": "Category I",
         "category_4_title": "Category M",
         "category_5_title": "Category P",
         "category_1_descriptions": "Description 1",
         "category_2_descriptions": "Description X",
         "category_3_descriptions": "Description A",
         "category_4_descriptions": "Description M",
         "category_5_descriptions": "Description P"
      },
      {
         "title": "Today's Money 2",
         "value": "$30k",
         "icon": "home",
         "change_class": "warning",
         "change": "+15%",
         "description": "compared to last month",
         "product_uuid": "02a573f8-0db0-4d07-b31d-713a8b61c5d8",
         "category_1_title": "Category B",
         "category_2_title": "Category Y",
         "category_3_title": "Category II",
         "category_4_title": "Category N",
         "category_5_title": "Category Q",
         "category_1_descriptions": "Description 2",
         "category_2_descriptions": "Description Y",
         "category_3_descriptions": "Description B",
         "category_4_descriptions": "Description N",
         "category_5_descriptions": "Description Q"
      },
      {
         "title": "Today's Money 3",
         "value": "$45k",
         "icon": "business",
         "change_class": "danger",
         "change": "+30%",
         "description": "since last quarter",
         "product_uuid": "5b93b02e-739b-4bb3-b07d-788c3ef5d1a6",
         "category_1_title": "Category C",
         "category_2_title": "Category Z",
         "category_3_title": "Category III",
         "category_4_title": "Category O",
         "category_5_title": "Category R",
         "category_1_descriptions": "Description 3",
         "category_2_descriptions": "Description Z",
         "category_3_descriptions": "Description C",
         "category_4_descriptions": "Description O",
         "category_5_descriptions": "Description R"
      },
      {
         "title": "Today's Money 4",
         "value": "$23k",
         "icon": "sports",
         "change_class": "success",
         "change": "+22%",
         "description": "than last week",
         "product_uuid": "15b75572-bec9-4a1a-9d35-5d587b00f2a4",
         "category_1_title": "Category A",
         "category_2_title": "Category X",
         "category_3_title": "Category I",
         "category_4_title": "Category M",
         "category_5_title": "Category P",
         "category_1_descriptions": "Description 1",
         "category_2_descriptions": "Description X",
         "category_3_descriptions": "Description A",
         "category_4_descriptions": "Description M",
         "category_5_descriptions": "Description P"
      },
      {
         "title": "Today's Money 5",
         "value": "$55k",
         "icon": "fitness",
         "change_class": "warning",
         "change": "+18%",
         "description": "compared to last month",
         "product_uuid": "edb2028a-dce9-48f9-805d-2fe9a45b9d42",
         "category_1_title": "Category B",
         "category_2_title": "Category Y",
         "category_3_title": "Category II",
         "category_4_title": "Category N",
         "category_5_title": "Category Q",
         "category_1_descriptions": "Description 2",
         "category_2_descriptions": "Description Y",
         "category_3_descriptions": "Description B",
         "category_4_descriptions": "Description N",
         "category_5_descriptions": "Description Q"
      },
      {
         "title": "Today's Money 6",
         "value": "$67k",
         "icon": "home",
         "change_class": "success",
         "change": "+40%",
         "description": "since last quarter",
         "product_uuid": "49ea74e4-68ab-4ad2-8c95-b8b7b78db237",
         "category_1_title": "Category C",
         "category_2_title": "Category Z",
         "category_3_title": "Category III",
         "category_4_title": "Category O",
         "category_5_title": "Category R",
         "category_1_descriptions": "Description 3",
         "category_2_descriptions": "Description Z",
         "category_3_descriptions": "Description C",
         "category_4_descriptions": "Description O",
         "category_5_descriptions": "Description R"
      },
      {
         "title": "Today's Money 7",
         "value": "$72k",
         "icon": "business",
         "change_class": "danger",
         "change": "+50%",
         "description": "than last week",
         "product_uuid": "5878b29f-8b1f-4cc4-bb53-6c324a4c4d5f",
         "category_1_title": "Category A",
         "category_2_title": "Category X",
         "category_3_title": "Category I",
         "category_4_title": "Category M",
         "category_5_title": "Category P",
         "category_1_descriptions": "Description 1",
         "category_2_descriptions": "Description X",
         "category_3_descriptions": "Description A",
         "category_4_descriptions": "Description M",
         "category_5_descriptions": "Description P"
      },
      {
         "title": "Today's Money 8",
         "value": "$80k",
         "icon": "weekend",
         "change_class": "success",
         "change": "+60%",
         "description": "compared to last month",
         "product_uuid": "02321fe6-5124-47f7-bb57-2be9c582fdb2",
         "category_1_title": "Category B",
         "category_2_title": "Category Y",
         "category_3_title": "Category II",
         "category_4_title": "Category N",
         "category_5_title": "Category Q",
         "category_1_descriptions": "Description 2",
         "category_2_descriptions": "Description Y",
         "category_3_descriptions": "Description B",
         "category_4_descriptions": "Description N",
         "category_5_descriptions": "Description Q"
      }
   ]

   data = []
   for product in datas:
      encoded_uuid = base64.urlsafe_b64encode(product['product_uuid'].encode()).decode('utf-8')

      data.append({
         'title': product['title'],
         'value': product['value'],
         'icon': product['icon'],
         'change_class': product['change_class'],
         'change': product['change'],
         'description': product['description'],
         'product_uuid': product['product_uuid'],
         'category_1_title': product['category_1_title'],
         'category_2_title': product['category_2_title'],
         'category_3_title': product['category_3_title'],
         'category_4_title': product['category_4_title'],
         'category_5_title': product['category_5_title'],
         'category_1_descriptions': product['category_1_descriptions'],
         'category_2_descriptions': product['category_2_descriptions'],
         'category_3_descriptions': product['category_3_descriptions'],
         'category_4_descriptions': product['category_4_descriptions'],
         'category_5_descriptions': product['category_5_descriptions']
      })

   return jsonify({
      'start': starting_id,
      'end': ending_id,
      'data': data,
      'template': render_template('components/load_data_templates/load_data_templates.html', data=data)
   }), 200



@bp.route('side_bar_by_user', methods=['POST'])   
def side_bar_by_user():
   product = request.get_json()
   template = render_template('components/load_data_templates/load_data_side_bar.html', data=product)

   return jsonify({
      'data': product,
      'template': template
   }), 200
    
