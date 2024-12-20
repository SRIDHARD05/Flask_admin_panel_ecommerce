from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("credits", __name__, url_prefix="/credits")


# TODO: Add the /credits/ page to Side Bar
@bp.route('/', methods=['POST','GET'])
def dashboard():
    return render_template('credits.html')



    