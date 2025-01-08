from flask import Blueprint, request, jsonify, render_template
import base64
from src.Save import Save

bp = Blueprint("save_posts", __name__, url_prefix="/save")

@bp.route('/')
def dashboard():
    return render_template('history.html', videos=data)

@bp.route('/user_save', methods=['POST'])
def user_save():
    jsonData = request.get_json()
    user_id = "w234567"
    # TODO: Based on the Adds/Products/Shopify
    media_type = 'sample'
    product_id = 'product_id'
    product_id_hash = jsonData['product_id']
    try:
        save_posts = Save.save_posts(user_id, media_type,product_id,product_id_hash)
        return jsonify({
            "status": 200,
            "message" : "Data Saved Successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "status": 400,
            "message": str(e),
        }), 400

@bp.route('/collection/create', methods=['POST'])
def create_collections():
    jsonData = request.get_json()
    collection_name = jsonData['collection_name']
    try:
        save_posts = Save.create_collections(user_id, collection_name)
        return jsonify({
            "status": 200,
            "message" : "Data Saved Successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "status": 400,
            "message": str(e),
        }), 400

@bp.route('/collection/show', methods=['POST'])
def save_collections():
    try:
        posts_collections = Save.get_saved_posts_collections(session['email'])
        return jsonify({
            "status": 200,
            "message" : "Data Saved Successfully",
            "data" : posts_collections
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": 400,
            "message": str(e),
        }), 400