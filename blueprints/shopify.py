from flask import Flask, request, jsonify, render_template, Blueprint
from bson import ObjectId, errors 
from src import login_required, user_required, admin_required 
from src.Shopify import Shopify

bp = Blueprint("shopify", __name__, url_prefix="/shopify")

"""
user Routes - 
    1. /best-shoify-apps
    2. 

Admin Routes - 
    1. /best-shoify-apps/save
"""

@bp.route("/best-shoify-apps", methods=["GET"])
@user_required
def view_best_apps():
    apps = Shopify.get_best_apps()
    return render_template('components/shopify/apps/view.html', apps=apps)


@bp.route("/best-shoify-apps/save", methods=["GET"])
@user_required
def view_best_apps_save():
    return render_template('components/shopify/apps/save.html')


@bp.route("/best-shoify-apps/save", methods=["POST"])
@admin_required
def save_best_apps():
    try:
        app_data = request.form.to_dict()
        data = Shopify.save_best_apps(app_data)
        return {'success':True, 'message':f"App saved successfully"}
    except Exception as e:
        return {'success':False, 'message':str(e)}



