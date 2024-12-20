import sys
# sys.path.append('/home/sibidharan/iotweb')

from flask import Flask
from flask import Flask, redirect, url_for, request, render_template, session
import os
import math
import base64
# from src import get_config
# from src.User import User
# from src.API import API
from blueprints import search_filters, products, videos, dashboard, users, pricing, save_posts, errors, credits

app = Flask(__name__, static_folder='assets')
# app.secret_key = get_config("secret_key")

@app.route('/')
def home():
    return {
        'page' : 'Home Page'
    }



@app.route('/videos')
def sample_page():
    return render_template('videos.html')


app.register_blueprint(search_filters.bp)
app.register_blueprint(products.bp)
app.register_blueprint(videos.bp)
app.register_blueprint(dashboard.bp)
app.register_blueprint(users.bp)
app.register_blueprint(pricing.bp)
app.register_blueprint(save_posts.bp)
app.register_blueprint(errors.bp)
app.register_blueprint(credits.bp)



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)