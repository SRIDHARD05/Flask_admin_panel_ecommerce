from flask import Blueprint, request, jsonify, render_template
import base64

bp = Blueprint("tools", __name__, url_prefix="/tools")


@bp.route('/')
def dashboard():
    return render_template('components/tools/dashboard.html')


@bp.route('/basic/calculate-profit', methods=['POST'])
def calculate_profit():
    try:
        data = request.get_json()
        
        product_cost = data.get('product_cost')
        selling_price = data.get('selling_price')
        
        if product_cost is None or selling_price is None:
            return jsonify({'message': 'Product cost and selling price are required'}), 400
        
        profit = selling_price - product_cost
        
        profit_margin = (profit / selling_price) * 100 if selling_price > 0 else 0
        
        return jsonify({
            'product_cost': product_cost,
            'selling_price': selling_price,
            'profit': profit,
            'profit_margin': profit_margin
        })
    
    except Exception as e:
        return jsonify({'message': f'Error occurred: {str(e)}', 'status': '500'}), 500


@bp.route('/pro/calculate-dropshipping-profit', methods=['POST'])
def calculate_dropshipping_profit():
    try:
        data = request.get_json()

        supplier_location = data.get('supplier_location')
        shop_currency = data.get('shop_currency')
        show_results_in_currency = data.get('show_results_in_currency')
        
        product_cost = float(data.get('product_cost', 0))
        advertising_cost = float(data.get('advertising_cost', 0))
        shipping_cost = float(data.get('shipping_cost', 0))
        other_cost = float(data.get('other_cost', 0))

        selling_price = float(data.get('selling_price', 0))
        shipping_revenues = float(data.get('shipping_revenues', 0))
        product_discounts = float(data.get('product_discounts', 0))

        total_costs = product_cost + advertising_cost + shipping_cost + other_cost
        total_revenues = selling_price + shipping_revenues - product_discounts

        profit = total_revenues - total_costs

        profit_margin = (profit / total_revenues) * 100 if total_revenues > 0 else 0

        return jsonify({
            'supplier_location': supplier_location,
            'shop_currency': shop_currency,
            'show_results_in_currency': show_results_in_currency,
            'product_cost': product_cost,
            'advertising_cost': advertising_cost,
            'shipping_cost': shipping_cost,
            'other_cost': other_cost,
            'selling_price': selling_price,
            'shipping_revenues': shipping_revenues,
            'product_discounts': product_discounts,
            'total_costs': total_costs,
            'total_revenues': total_revenues,
            'profit': profit,
            'profit_margin': profit_margin
        })
    
    except Exception as e:
        return jsonify({'message': f'Error occurred: {str(e)}', 'status': '500'}), 500


@bp.route('/calculate-max-shopify-sales', methods=['POST'])
def calculate_max_shopify_sales():
    try:
        data = request.get_json()

        traffic_limit = float(data.get('traffic_limit', 0))
        conversion_rate = float(data.get('conversion_rate', 0.05))  

        max_sales = traffic_limit * conversion_rate
        
        return jsonify({
            'traffic_limit': traffic_limit,
            'conversion_rate': conversion_rate * 100,  
            'max_sales': max_sales
        })
    
    except Exception as e:
        return jsonify({'message': f'Error occurred: {str(e)}', 'status': '500'}), 500


"""
## Best Open-Source APIs for Trademark Searches
****1. Markify Trademark Search API:****
****2. Indian Trademark Search API:****
****3. Zyla Trademark Search API:****
****4. USPTO TSDR Data API:****
****5. TMSearch.ai:****

"""