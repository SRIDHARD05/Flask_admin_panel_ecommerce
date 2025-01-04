from flask import Blueprint, request, jsonify, render_template
import base64

bp = Blueprint("videos", __name__, url_prefix="/videos")

