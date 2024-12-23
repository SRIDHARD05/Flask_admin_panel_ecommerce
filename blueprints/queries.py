from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("queries", __name__, url_prefix="/queries")


@bp.route('/')
def sample_page():
    return {
        'message' : 'this is a query pages',
        'status' : 'success'
    }