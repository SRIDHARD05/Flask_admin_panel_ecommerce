from flask import Blueprint, request, jsonify, render_template
import base64

bp = Blueprint("pricing", __name__, url_prefix="/pricing")


@bp.route('/')
def dashboard():
    return render_template('billing.html')