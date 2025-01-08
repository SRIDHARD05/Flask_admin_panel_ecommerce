from flask import Blueprint, request, jsonify, render_template
from flask import Flask, redirect, url_for, request, render_template, session, jsonify,Blueprint
import base64
from src.User import User
from src.Profile import Profile

bp = Blueprint("profile", __name__, url_prefix="/profile")

@bp.route('/')
def home():
    user_data = Profile.get_user_profile(session['email'])
    # print(user_data)
    return render_template('profile.html',user_data = user_data,session = session)


@bp.route("/user/save", methods=['POST','GET'])
def save():
    data = request.get_json() 
    if 'first_name' in data and 'last_name' in data and 'email' in data and 'location' in data and 'phonenumber' in data:
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        location = data['location']
        phonenumber = data['phonenumber']
        try:
            uid = Profile.save_user(first_name, last_name, email, location, phonenumber)
            # print(uid)
            return jsonify({
                "status": 200,
                "user_id": uid
            }), 200
        except Exception as e:
            return jsonify({
                "status": 400,
                "message": str(e),
            }), 400
    else:
        return jsonify({
            "message": "Not enough parameters",
        }), 400




@bp.route("/reset_password", methods=['POST'])
def reset_password():
    data = request.get_json()
    print('data:', data)

    new_password = data['new_password']
    old_password = data['old_password']
    email = session['email']

    if not email:
        return jsonify({"status": 400, "message": "User not logged in"}), 400

    if not new_password or not old_password:
        return jsonify({"status": 400, "message": "Old and new passwords are required"}), 400

    try:
        response = Profile.reset_password(email, old_password, new_password)
        return jsonify(response), response["status"]
    except Exception as e:
        return jsonify({"status": 400, "message": str(e)}), 400
