from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route('/signin')
def signin():
    return render_template('sign_in.html')


@bp.route('/signup')
def signup():
    return render_template('sign_up.html')

# TODO: Reset Password Templates
@bp.route('/reset_password')
def reset_password():
    return render_template('reset_password.html')