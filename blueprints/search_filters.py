from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("search_filters", __name__, url_prefix="/search_filters")


@bp.route('load_data', methods=['POST'])  
def load_data():
   data = request.get_json() 
   starting_id = data.get("starting_id", "")
   ending_id = data.get("ending_id", "")


   # TODO:  Fetch the Datas from the database
   # load_data = Load_data().load_data(starting_id,ending_id)
   
   # TODO: Fetch the templates and append the databases from the db to templates
   # TODO: Implement encode the PRoduct UUID to Avaoid the UUID Hijacking
   datas = [
      {"title": "Today's Money", "value": "$53k", "icon": "weekend", "change_class": "success", "change": "+55%", "description": "than last week", "product_uuid": "123e4567-e89b-12d3-a456-426614174000"},
      {"title": "Today's Users", "value": "2300", "icon": "person", "change_class": "success", "change": "+3%", "description": "than last month", "product_uuid": "123e4567-e89b-12d3-a456-426614174001"},
      {"title": "Ads Views", "value": "3,462", "icon": "leaderboard", "change_class": "danger", "change": "-2%", "description": "than yesterday", "product_uuid": "123e4567-e89b-12d3-a456-426614174002"},
      {"title": "Total Sales", "value": "$18k", "icon": "shopping_cart", "change_class": "success", "change": "+12%", "description": "compared to last month", "product_uuid": "123e4567-e89b-12d3-a456-426614174003"},
      {"title": "Active ", "value": "1,280", "icon": "subscriptions", "change_class": "success", "change": "+5%", "description": "since last week", "product_uuid": "123e4567-e89b-12d3-a456-426614174004"},
      {"title": "Customer ", "value": "35", "icon": "help_outline", "change_class": "danger", "change": "-8%", "description": "from last month", "product_uuid": "123e4567-e89b-12d3-a456-426614174005"},
      {"title": "Site Traffic", "value": "56k", "icon": "traffic", "change_class": "success", "change": "+10%", "description": "since last week", "product_uuid": "123e4567-e89b-12d3-a456-426614174006"},
      {"title": "New Signups", "value": "950", "icon": "person_add", "change_class": "success", "change": "+4%", "description": "since yesterday", "product_uuid": "123e4567-e89b-12d3-a456-426614174007"},
   ]


   data = []
   for product in datas:
      encoded_uuid = base64.urlsafe_b64encode(product['product_uuid'].encode()).decode('utf-8')

      # Prepare the data for rendering
      data.append({
         'title': product['title'],
         'value': product['value'],
         'icon': product['icon'],
         'change_class': product['change_class'],
         'change': product['change'],
         'description': product['description'],
         'product_uuid': encoded_uuid
      })

   return jsonify({
      'start': starting_id,
      'end': ending_id,
      'data': data,
      'template': render_template('components/load_data_templates/load_data_templates.html', data=data)
   }), 200


