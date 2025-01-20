from flask import Blueprint, request, jsonify, render_template
import base64
from src import login_required, user_required, admin_required 

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


@bp.route('/store/theme_analysis', methods=['GET'])
@user_required
def shopify_theme_detections():
    return render_template('components/shopify/themes/dashboard.html')


@bp.route('/store/theme_analysis', methods=['POST'])
@user_required
def shopify_theme_detections_result():
    data = request.get_json()
    url = data['url']
    print(url)
    return {
        'message' : 'success',
        'status' : '200'
    }



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

