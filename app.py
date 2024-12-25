import sys
from flask import Flask, redirect, url_for, request, render_template, session, jsonify
import os
import math
import base64
import time
from blueprints import search_filters, products, videos, dashboard, users, pricing, save_posts, errors, credits, sidebar, queries
import json
import pandas as pd
from datetime import datetime
import subprocess

app = Flask(__name__, static_folder='assets', static_url_path="/")

@app.route('/')
def home():
    return {
        'page' : 'Home Page'
    }

@app.route('/videos')
def sample_page():
    return render_template('videos.html')

@app.route('/popover')
def popover():
    return render_template('popovers.html')

@app.route('/test2')
def test3():
    return render_template('test3.html')


@app.route('/test/functions', methods=['GET'])
def process_completions():
    # Define your URLs to test
    urls = [
        "https://spicestore.stanford.edu"
    ]

    # Create a name for the report files
    name = "LighthouseReport"
    getdate = datetime.now().strftime("%Y-%m-%d")

    try:
        # Loop through each URL and run Lighthouse
        for url in urls:
            output_path = f"{name}_{getdate}.report.json"
            command = f'lighthouse {url} --output=json --output-path={output_path} --chrome-flags="--headless"'

            # Run Lighthouse using subprocess
            try:
                subprocess.check_output(command, shell=True, text=True)
                print(f"Lighthouse command completed for URL: {url}")
            except subprocess.CalledProcessError as e:
                print(f"Error executing Lighthouse command for {url}: {e}")
                return jsonify({
                    'status': '500',
                    'message': f"Error executing command for {url}",
                    'error': str(e)
                }), 500

            # Check if the JSON file is created
            if os.path.exists(output_path):
                print(f"JSON report created: {output_path}")
                # Return success response immediately after the JSON file is created
                return jsonify({
                    'status': '200',
                    'message': f"JSON report created: {output_path}"
                }), 200
            else:
                print(f"JSON report not found: {output_path}")
                return jsonify({
                    'status': '404',
                    'message': f"JSON report not found for {url}"
                }), 404

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({
            'status': '500',
            'message': 'Unexpected error occurred',
            'error': str(e)
        }), 500


@app.route('/test')
def test():
    datas = [
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 120,
            "shares": 30,
            "comments": 15,
            "like_thumb": "path/to/like_thumb.jpg",
            "share_thumb": "path/to/share_thumb.jpg",
            "title": "Today's Money 1",
            "comment_thumb": "path/to/comment_thumb.jpg",
            "value": "$12k",
            "icon": "weekend",
            "change_class": "success",
            "change": "+12%",
            "description": "than last week",
            "product_uuid": "f91e4c65-2d45-45d1-bf6c-c89cbb9579f4",
            "category_1_title": "Category A",
            "category_2_title": "Category X",
            "category_3_title": "Category I",
            "category_4_title": "Category M",
            "category_5_title": "Category P",
            "category_1_descriptions": "Description 1",
            "category_2_descriptions": "Description X",
            "category_3_descriptions": "Description A",
            "category_4_descriptions": "Description M",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description P",
            "saved_dated" : "12-04-2003"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 200,
            "shares": 45,
            "comments": 30,
            "like_thumb": "path/to/like_thumb_2.jpg",
            "share_thumb": "path/to/share_thumb_2.jpg",
            "title": "Today's Money 2",
            "comment_thumb": "path/to/comment_thumb_2.jpg",
            "value": "$15k",
            "icon": "trending_up",
            "change_class": "success",
            "change": "+15%",
            "description": "since last month",
            "product_uuid": "c3c92f45-3e8c-48b3-a9d7-b15b2897adfe",
            "category_1_title": "Category B",
            "category_2_title": "Category Y",
            "category_3_title": "Category II",
            "category_4_title": "Category N",
            "category_5_title": "Category Q",
            "category_1_descriptions": "Description B",
            "category_2_descriptions": "Description Y",
            "category_3_descriptions": "Description II",
            "category_4_descriptions": "Description N",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description Q"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 310,
            "shares": 80,
            "comments": 50,
            "like_thumb": "path/to/like_thumb_3.jpg",
            "share_thumb": "path/to/share_thumb_3.jpg",
            "title": "Today's Money 3",
            "comment_thumb": "path/to/comment_thumb_3.jpg",
            "value": "$22k",
            "icon": "star",
            "change_class": "success",
            "change": "+20%",
            "description": "compared to last quarter",
            "product_uuid": "742c52b7-68de-4b70-9fc7-8ffb3e372fbd",
            "category_1_title": "Category C",
            "category_2_title": "Category Z",
            "category_3_title": "Category III",
            "category_4_title": "Category O",
            "category_5_title": "Category R",
            "category_1_descriptions": "Description C",
            "category_2_descriptions": "Description Z",
            "category_3_descriptions": "Description III",
            "category_4_descriptions": "Description O",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description R"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 50,
            "shares": 10,
            "comments": 5,
            "like_thumb": "path/to/like_thumb_4.jpg",
            "share_thumb": "path/to/share_thumb_4.jpg",
            "title": "Today's Money 4",
            "comment_thumb": "path/to/comment_thumb_4.jpg",
            "value": "$5k",
            "icon": "attach_money",
            "change_class": "danger",
            "change": "-5%",
            "description": "lower than last year",
            "product_uuid": "d0b8a7f6-7203-4695-bb5e-f2cdad1b1fdf",
            "category_1_title": "Category D",
            "category_2_title": "Category W",
            "category_3_title": "Category IV",
            "category_4_title": "Category T",
            "category_5_title": "Category S",
            "category_1_descriptions": "Description D",
            "category_2_descriptions": "Description W",
            "category_3_descriptions": "Description IV",
            "category_4_descriptions": "Description T",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description S"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 420,
            "shares": 90,
            "comments": 60,
            "like_thumb": "path/to/like_thumb_5.jpg",
            "share_thumb": "path/to/share_thumb_5.jpg",
            "title": "Today's Money 5",
            "comment_thumb": "path/to/comment_thumb_5.jpg",
            "value": "$30k",
            "icon": "show_chart",
            "change_class": "success",
            "change": "+25%",
            "description": "exceeded expectations",
            "product_uuid": "457d6b12-3b33-42ac-b5e2-0a1e6e17c875",
            "category_1_title": "Category E",
            "category_2_title": "Category V",
            "category_3_title": "Category V",
            "category_4_title": "Category U",
            "category_5_title": "Category D",
            "category_1_descriptions": "Description E",
            "category_2_descriptions": "Description V",
            "category_3_descriptions": "Description V",
            "category_4_descriptions": "Description U",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description D"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 350,
            "shares": 50,
            "comments": 25,
            "like_thumb": "path/to/like_thumb_6.jpg",
            "share_thumb": "path/to/share_thumb_6.jpg",
            "title": "Today's Money 6",
            "comment_thumb": "path/to/comment_thumb_6.jpg",
            "value": "$18k",
            "icon": "access_alarm",
            "change_class": "success",
            "change": "+18%",
            "description": "better than expected",
            "product_uuid": "ce9c5d99-f303-4388-bd6f-7e912c9fa1ab",
            "category_1_title": "Category F",
            "category_2_title": "Category W",
            "category_3_title": "Category VI",
            "category_4_title": "Category Y",
            "category_5_title": "Category T",
            "category_1_descriptions": "Description F",
            "category_2_descriptions": "Description W",
            "category_3_descriptions": "Description VI",
            "category_4_descriptions": "Description Y",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description T"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 180,
            "shares": 40,
            "comments": 22,
            "like_thumb": "path/to/like_thumb_7.jpg",
            "share_thumb": "path/to/share_thumb_7.jpg",
            "title": "Today's Money 7",
            "comment_thumb": "path/to/comment_thumb_7.jpg",
            "value": "$8k",
            "icon": "business_center",
            "change_class": "warning",
            "change": "+8%",
            "description": "increased slightly",
            "product_uuid": "8fb13bb7-6791-45a5-8882-33d69f2d9f64",
            "category_1_title": "Category G",
            "category_2_title": "Category P",
            "category_3_title": "Category VII",
            "category_4_title": "Category Z",
            "category_5_title": "Category J",
            "category_1_descriptions": "Description G",
            "category_2_descriptions": "Description P",
            "category_3_descriptions": "Description VII",
            "category_4_descriptions": "Description Z",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description J"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 500,
            "shares": 100,
            "comments": 80,
            "like_thumb": "path/to/like_thumb_8.jpg",
            "share_thumb": "path/to/share_thumb_8.jpg",
            "title": "Today's Money 8",
            "comment_thumb": "path/to/comment_thumb_8.jpg",
            "value": "$45k",
            "icon": "attach_money",
            "change_class": "success",
            "change": "+30%",
            "description": "massive increase",
            "product_uuid": "fa27b4a9-b4a0-4676-bf4b-d27c7c219f92",
            "category_1_title": "Category H",
            "category_2_title": "Category Q",
            "category_3_title": "Category VIII",
            "category_4_title": "Category L",
            "category_5_title": "Category W",
            "category_1_descriptions": "Description H",
            "category_2_descriptions": "Description Q",
            "category_3_descriptions": "Description VIII",
            "category_4_descriptions": "Description L",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description W"
        },
        {
            "src": "/videos/videoplayback_1.mp4",
            "height": 300,
            "likes": 500,
            "shares": 100,
            "comments": 80,
            "like_thumb": "path/to/like_thumb_8.jpg",
            "share_thumb": "path/to/share_thumb_8.jpg",
            "title": "Today's Money 8",
            "comment_thumb": "path/to/comment_thumb_8.jpg",
            "value": "$45k",
            "icon": "attach_money",
            "change_class": "success",
            "change": "+30%",
            "description": "massive increase",
            "product_uuid": "fa27b4a9-b4a0-4676-bf4b-d27c7c219f92",
            "category_1_title": "Category H",
            "category_2_title": "Category Q",
            "category_3_title": "Category VIII",
            "category_4_title": "Category L",
            "category_5_title": "Category W",
            "category_1_descriptions": "Description H",
            "category_2_descriptions": "Description Q",
            "category_3_descriptions": "Description VIII",
            "category_4_descriptions": "Description L",
            "saved_dated" : "12-04-2003",
            "category_5_descriptions": "Description W"
        }
    ]

    data = []
    for product in datas:
        encoded_uuid = base64.urlsafe_b64encode(product['product_uuid'].encode()).decode('utf-8')

        data.append({
            "src": product['src'],
            "height": product['height'],
            "likes": product['likes'],
            "shares": product['shares'],
            "comments": product['comments'],
            "like_thumb": product['like_thumb'],
            "share_thumb": product['share_thumb'],
            "comment_thumb": product['comment_thumb'],
            'title': product['title'],
            'value': product['value'],
            'icon': product['icon'],
            'change_class': product['change_class'],
            'change': product['change'],
            'description': product['description'],
            'product_uuid': product['product_uuid'],
            'category_1_title': product['category_1_title'],
            'category_2_title': product['category_2_title'],
            'category_3_title': product['category_3_title'],
            'category_4_title': product['category_4_title'],
            'category_5_title': product['category_5_title'],
            'category_1_descriptions': product['category_1_descriptions'],
            'category_2_descriptions': product['category_2_descriptions'],
            'category_3_descriptions': product['category_3_descriptions'],
            'category_4_descriptions': product['category_4_descriptions'],
            'category_5_descriptions': product['category_5_descriptions']
    })

    return render_template('test.html', videos=data)



@app.route('/loader')
def loader():
    return render_template('components/loaders/loader.html')


app.register_blueprint(search_filters.bp)
app.register_blueprint(products.bp)
app.register_blueprint(videos.bp)
app.register_blueprint(dashboard.bp)
app.register_blueprint(users.bp)
app.register_blueprint(pricing.bp)
app.register_blueprint(save_posts.bp)
app.register_blueprint(errors.bp)
app.register_blueprint(credits.bp)
app.register_blueprint(queries.bp)
app.register_blueprint(sidebar.bp)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)




