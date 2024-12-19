from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route('/<string:product_name>/<string:product_uuid>/show', methods=['POST','GET'])
def products_data(product_name, product_uuid):
    if request.method == 'POST':
        data = request.get_json()
        # return jsonify({
        #     'product_name': product_name,
        #     'product_uuid': product_uuid,
        #     'url': data['url'],
        #     'data' : data
        # }), 200
        return render_template('show_product.html',data=data)

    elif request.method == 'GET':
        return render_template('show_product.html')