from flask import Blueprint, request, jsonify, render_template, session
from src import *
from src.Ads_data import Ads_data

bp = Blueprint("ads_data", __name__, url_prefix="/ads_data")


@bp.route('/facebook/ads/store', methods=['POST'])
@user_required
def dashboard():
    jsonData = request.get_json()
    collection_name = jsonData.get('name')  # Name of the Facebook ad collection
    email = session.get('email')  # Email of the logged-in user

    if not email:
        return jsonify({
            "status": 400,
            "message": "User email not found in session."
        }), 400

    try:
        result = Ads_data.store_facebook_ads(email, collection_name, jsonData)
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


@bp.route("/", methods=["GET"])
@user_required
def view_best_apps():
    return  {
        'Page' : "This is a Ads Page"
    }