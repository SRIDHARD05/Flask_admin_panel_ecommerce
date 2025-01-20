from flask import Blueprint, request, jsonify, render_template
import base64
from src import login_required, user_required, admin_required 
import requests
import re
from bs4 import BeautifulSoup

bp = Blueprint("tools", __name__, url_prefix="/tools")


@bp.route('/')
@user_required
def dashboard():
    return render_template('components/tools/dashboard.html')


@bp.route('/basic/calculate-dropshipping-profit', methods=['GET'])
@user_required
def calculate_profit():
    return render_template('components/tools/basic_profit_calculater.html') 


@bp.route('/pro/calculate-dropshipping-profit', methods=['GET'])
@user_required
def calculate_dropshipping_profit():
    return render_template('components/tools/pro_profit_calculater.html')


@bp.route('/store/theme_detector', methods=['GET'])
@user_required
def shopify_theme_detections():
    return render_template('components/shopify/themes/dashboard.html')


@bp.route('/store/theme_detector', methods=['POST'])
@user_required
def shopify_theme_detections_result():
    data = request.get_json()
    url = data['url']

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'message': 'Failed to fetch the page', 'status': '500'}), 500

        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')

        theme_name = None
        theme_version = None

        theme_name_match = re.search(r'window\.BOOMR\.themeName\s*=\s*"(.*?)"', html_content)
        theme_version_match = re.search(r'window\.BOOMR\.themeVersion\s*=\s*"(.*?)"', html_content)

        if theme_name_match:
            theme_name = theme_name_match.group(1)
        if theme_version_match:
            theme_version = theme_version_match.group(1)

        if theme_name and theme_version:
            return jsonify({
                'message': 'success',
                'status': 200,
                'theme_name': theme_name,
                'theme_version': theme_version
            })
        if theme_name is None and theme_version is None:
            return jsonify({'message': 'Theme name/version not found', 'status': 404}), 200
    
    except Exception as e:
        return jsonify({'message': f'Error occurred: {str(e)}', 'status': '500'}), 500



# @bp.route('/calculate-max-shopify-sales', methods=['POST'])
# def calculate_max_shopify_sales():
#     try:
#         data = request.get_json()

#         traffic_limit = float(data.get('traffic_limit', 0))
#         conversion_rate = float(data.get('conversion_rate', 0.05))  

#         max_sales = traffic_limit * conversion_rate
        
#         return jsonify({
#             'traffic_limit': traffic_limit,
#             'conversion_rate': conversion_rate * 100,  
#             'max_sales': max_sales
#         })
    
#     except Exception as e:
#         return jsonify({'message': f'Error occurred: {str(e)}', 'status': '500'}), 500

"""
## Best Open-Source APIs for Trademark Searches
****1. Markify Trademark Search API:****
****2. Indian Trademark Search API:****
****3. Zyla Trademark Search API:****
****4. USPTO TSDR Data API:****
****5. TMSearch.ai:****
"""

