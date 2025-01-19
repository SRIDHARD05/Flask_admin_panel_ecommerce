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
    1. 
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
