from flask import Flask, redirect, url_for, request, render_template, session, jsonify,Blueprint
import base64
from src.Database import Database
from src.User import User
bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route('/')
def index():
    videos = [
        {
            'product_uuid': 1, 'src': '/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 120, 'shares': 30, 'comments': 15,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 2, 'src': '/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 200, 'shares': 50, 'comments': 25,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 3, 'src': '/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 150, 'shares': 40, 'comments': 20,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 4, 'src': '/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 180, 'shares': 45, 'comments': 22,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        }
    ]
    user_data = User.get_user()
    return render_template('dashboard.html', videos=videos,session = session,user_data = user_data)


# TODO: For Accessing the DevTools based on the User Roles
@bp.route('/user_validations', methods=['GET'])
def user_validations():
    user_data = User.get_user()
    if not user_data:
        return jsonify({'result': False, 'error': 'User not authenticated'}), 401

    user_role = user_data['role']
    if user_role in ['admin', 'developer']:
        return jsonify({'result': True}), 200
    else:
        User.log_unauthorized_attempt(user_data)
        return jsonify({'result': False}), 403


