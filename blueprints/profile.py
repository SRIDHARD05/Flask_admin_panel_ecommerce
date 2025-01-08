from flask import Blueprint, request, jsonify, render_template
from flask import Flask, redirect, url_for, request, render_template, session, jsonify
import base64
from src.User import User
from src.Profile import Profile

bp = Blueprint("profile", __name__, url_prefix="/profile")

@bp.route('/')
def home():
    user_data = User.get_user()
    return render_template('profile.html',user_data = user_data)


@bp.route("/user/save", methods=['POST'])
def save():
    if 'first_name' in request.form and 'last_name' in request.form and 'email' in request.form and 'location' in request.form and 'phonenumber' in request.form:
        first_name = request.form['firstname']
        last_name = request.form['last_name']
        email = request.form['email']
        location = request.form['location']
        phonenumber = request.form['phonenumber']
        try:
            uid = Profile.save_user(first_name,last_name,email,location,phonenumber)
            return {
                "status" : 200,
                "user_id": uid
            }, 200
        except Exception as e:
            return {
                "status" : 400,
                "message": str(e),
            }, 400
    else:
        return {
            "message": "Not enough parameters",
        }, 400