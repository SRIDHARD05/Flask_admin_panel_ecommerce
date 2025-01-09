from flask import Blueprint, request, jsonify, render_template
import base64

bp = Blueprint("tools", __name__, url_prefix="/tools")



@bp.route('/')
def dashboard():
    return render_template('components/tools/dashboard.html')