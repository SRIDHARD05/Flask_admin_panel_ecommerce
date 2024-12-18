from flask import Blueprint, render_template, redirect, url_for, request, session
from src.User import User
from src.Group import Group
from src.API import API
from src import md5_hash, time_ago, mask

bp = Blueprint("home", __name__, url_prefix="/")



@bp.route("/dashboard")
def dashboard():
   return render_template('dashboard.html', session=session)

