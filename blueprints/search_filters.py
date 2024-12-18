from flask import Blueprint, request, jsonify, render_template

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

   data = [
      {"title": "Today's Money", "value": "$53k", "icon": "weekend", "change_class": "success", "change": "+55%", "description": "than last week"},
      {"title": "Today's Users", "value": "2300", "icon": "person", "change_class": "success", "change": "+3%", "description": "than last month"},
      {"title": "Ads Views", "value": "3,462", "icon": "leaderboard", "change_class": "danger", "change": "-2%", "description": "than yesterday"},
      {"title": "Sales", "value": "$103,430", "icon": "weekend", "change_class": "success", "change": "+5%", "description": "than yesterday"},
      {"title": "Revenue", "value": "$45k", "icon": "bar_chart", "change_class": "success", "change": "+12%", "description": "than last month"},
      {"title": "New Clients", "value": "320", "icon": "person_add", "change_class": "success", "change": "+10%", "description": "than last week"},
      {"title": "Feedback", "value": "1,200", "icon": "feedback", "change_class": "success", "change": "+8%", "description": "than last month"},
      {"title": "Completed Orders", "value": "750", "icon": "done_all", "change_class": "success", "change": "+15%", "description": "than last month"}
   ]
   return jsonify({
      'start': starting_id,
      'end': ending_id,
      'template' : render_template('components/load_data_templates/load_data_templates.html', data=data)
   }), 200
