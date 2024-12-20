from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route('/')
def index():
    videos = [
        {
            'product_uuid': 1, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 120, 'shares': 30, 'comments': 15,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 2, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 200, 'shares': 50, 'comments': 25,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 3, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 150, 'shares': 40, 'comments': 20,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'product_uuid': 4, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 180, 'shares': 45, 'comments': 22,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'title' : 'sample_title',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        # {
        #     'product_uuid': 5, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 220, 'shares': 60, 'comments': 30,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 6, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 250, 'shares': 70, 'comments': 35,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 7, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 160, 'shares': 55, 'comments': 28,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 8, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 130, 'shares': 33, 'comments': 18,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 9, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 210, 'shares': 58, 'comments': 32,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 10, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 190, 'shares': 52, 'comments': 27,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 11, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 210, 'shares': 65, 'comments': 38,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 12, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 180, 'shares': 50, 'comments': 22,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 13, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 240, 'shares': 75, 'comments': 45,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 14, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 200, 'shares': 65, 'comments': 35,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 15, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 230, 'shares': 80, 'comments': 40,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 16, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 170, 'shares': 45, 'comments': 20,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 17, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 280, 'shares': 95, 'comments': 50,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 18, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 260, 'shares': 72, 'comments': 38,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 19, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 220, 'shares': 60, 'comments': 33,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # },
        # {
        #     'product_uuid': 20, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
        #     'likes': 210, 'shares': 68, 'comments': 41,
        #     'like_thumb': 'path/to/like_thumb.jpg',
        #     'share_thumb': 'path/to/share_thumb.jpg',
        #     'title' : 'sample_title',
        #     'comment_thumb': 'path/to/comment_thumb.jpg'
        # }
    ]

    return render_template('dashboard.html', videos=videos)

