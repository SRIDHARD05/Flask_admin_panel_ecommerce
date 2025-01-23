import sys
from flask import Flask, redirect, url_for, request, render_template, session, jsonify
import os
import math
import base64
import time
from blueprints import search_filters, products, videos, dashboard, users, pricing, save_posts, credits, sidebar, queries, shopify_seo, profile, tools, testsfile, admin, shopify, stores
import json
import pandas as pd
from datetime import datetime
import subprocess
from src import get_config



app = Flask(__name__, static_folder='assets', static_url_path="/")

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  
app.config['SECRET_KEY'] = get_config("user_secret")
app.config['SESSION_COOKIE_SECURE'] = True  
app.config['SESSION_COOKIE_HTTPONLY'] = True  
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 
# TODO: After change it to Productions
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return {
        'page' : 'Home Page'
    }

# @app.route('/videos')
# def sample_page():
#     return render_template('videos.html')



# @app.route('/popover')
# def popover():
#     return render_template('popovers.html')

@app.route('/test2')
def test3():
    return render_template('test3.html')

@app.route('/test')
def test():
    return render_template('test.html' ,session= session)


@app.route('/loader')
def loader():
    return render_template('components/loaders/loader.html')

@app.route('/dev_tools_loader')
def dev_tools_loader():
    return render_template('components/tools/dev_tools_loader.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('components/error/error_404.html'), 404

@app.errorhandler(500)
def page_not__found(e):
    return render_template('components/error/error_500.html'), 500


@app.route('/unauthorized')
def unauthorized():
    return render_template('components/error/unautherized.html')

@app.route('/signin')
def signin():
    return render_template('sign_in.html')


@app.route('/signup')
def signup():
    return render_template('sign_up.html')

"""
TODO: For Page Prefix based Error Pages

@app.errorhandler(404)
def page_not_found(e):
    # if a request is in our blog URL space
    if request.path.startswith('/blog/'):
        # we return a custom blog 404 page
        return render_template("blog/404.html"), 404
    else:
        # otherwise we return our generic site-wide 404 page
        return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    # if a request has the wrong method to our API
    if request.path.startswith('/api/'):
        # we return a json saying so
        return jsonify(message="Method Not Allowed"), 405
    else:
        # otherwise we return a generic site-wide 405 page
        return render_template("405.html"), 405

"""
app.register_blueprint(search_filters.bp)
app.register_blueprint(products.bp)
app.register_blueprint(videos.bp)
app.register_blueprint(dashboard.bp)
app.register_blueprint(users.bp)
app.register_blueprint(pricing.bp)
app.register_blueprint(save_posts.bp)
app.register_blueprint(credits.bp)
app.register_blueprint(queries.bp)
app.register_blueprint(sidebar.bp)
app.register_blueprint(shopify_seo.bp)
app.register_blueprint(profile.bp)
app.register_blueprint(tools.bp)
app.register_blueprint(testsfile.bp)   
app.register_blueprint(admin.bp) 
app.register_blueprint(shopify.bp) 
app.register_blueprint(stores.bp)




# if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=7000, debug=True,ssl_context='adhoc')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7345, debug=True)
