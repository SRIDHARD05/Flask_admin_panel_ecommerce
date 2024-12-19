from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("videos", __name__, url_prefix="/videos")

