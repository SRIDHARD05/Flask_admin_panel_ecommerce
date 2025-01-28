from flask import Blueprint, request, jsonify, render_template, session
from src import *
from src.Ads_data import Ads_data

bp = Blueprint("ads_data", __name__, url_prefix="/ads_data")


@bp.route('/facebook/ads/store', methods=['POST'])
@admin_required
def store_facebook_ads():
    try:
        jsonData = request.get_json()
        collection_name = jsonData.get('name') 
        email = session.get('email')  

        if not email:
            return jsonify({
                "status": 400,
                "message": "User email not found in session."
            }), 400

        result = Ads_data.store_facebook_ads(email, collection_name, jsonData)
        print(result , '/n')
        if result["success"]:
            return jsonify({
                "status": 200,
                "message": result["message"]
            }), 200
        else:
            return jsonify({
                "status": 400,
                "message": result["message"]
            }), 400
    except Exception as e:
        return jsonify({
            "status": 500,
            "message": str(e)
        }), 500



@bp.route("/facebook/ads/store", methods=["GET"])
@admin_required
def save_face_books_ads():
    return render_template("components/ads/facebook/save.html")


@bp.route('/facebook/ads/bulk/upload', methods=['POST'])
@admin_required
def bulk_upload_ads():
    try:
        bulk_data = request.get_json()
        # print(bulk_data) 

        if not bulk_data or not isinstance(bulk_data, list):
            return jsonify({
                "status": 400,
                "message": "Invalid data format. Expected an array of JSON objects."
            }), 400

        result = Ads_data.bulk_facebook_ads(bulk_data)
        
        if result["status"] == "error":
            return jsonify(result), 400

        return jsonify({
            "status": 200,
            "message": "Bulk upload successful.",
            "result_ids": result['result_id']  
        }), 200

    except Exception as e:
        return jsonify({
            "status": 500,
            "message": str(e)
        }), 500

