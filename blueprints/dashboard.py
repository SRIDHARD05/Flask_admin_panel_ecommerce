from flask import Blueprint, request, jsonify, render_template
import base64


from src.Load_data import Load_data
bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


# @bp.route('/')
# def home():
#     datas = [
#         {'id': 'zr905ygis7', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 400},
#         {'id': 'sqxcwdc8wo', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 350},
#         {'id': '3mb5lfum5h', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 450},
#         {'id': 'uptetshoc2', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 420},
#         {'id': 'ky28reuaxh', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 380},
#         {'id': 'pw9avba0a8', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 400},
#         {'id': 'ccb7w0a3my', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 450},
#         {'id': '6jx55xgwku', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 470},
#         {'id': 'bwvvnvzbnl', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 390},
#         {'id': 'cw48qitcer', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 420},
#         {'id': 'sz9d3jj60i', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 430},
#         {'id': 'mtbo6zqufk', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 440},
#         {'id': 'tewycnzcda', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 450},
#         {'id': 'ww3plmnpr8', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 470},
#         {'id': 'okeg89sm64', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 460},
#         {'id': 'tcdn7brljm', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 410},
#         {'id': 'aq61j9oaq9', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 440},
#         {'id': 'ey0r5rcr1m', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 420},
#         {'id': 'yru99ikcv5', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 430},
#         {'id': 'bgqtzau5it', 'src': '/assets/videos/videoplayback_1.mp4', 'height': 460}
#     ]

#     return render_template('dashboard.html', videos=datas)

@bp.route('/')
def index():
    # Sample video data including likes, shares, and comments
    videos = [
        {
            'id': 1, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 120, 'shares': 30, 'comments': 15,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        {
            'id': 2, 'src': '/assets/videos/videoplayback_1.mp4', 'height': 300, 
            'likes': 200, 'shares': 50, 'comments': 25,
            'like_thumb': 'path/to/like_thumb.jpg',
            'share_thumb': 'path/to/share_thumb.jpg',
            'comment_thumb': 'path/to/comment_thumb.jpg'
        },
        # More video data
    ]
    return render_template('dashboard.html', videos=videos)

