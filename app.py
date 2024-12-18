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
from blueprints import search_filters

app = Flask(__name__, static_folder='assets')
# app.secret_key = get_config("secret_key")

@app.route('/')
def home():
    # Rendering the template for the home page
    return render_template('dashboard.html')

app.register_blueprint(search_filters.bp)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)