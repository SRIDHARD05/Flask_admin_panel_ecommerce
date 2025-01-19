from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash,session
import base64
from src.User import User
from src.Session import Session
from src import *

bp = Blueprint("admin", __name__, url_prefix="/admin")


# TODO: Reset Password Templates   

@bp.route('/dashboard')
@admin_required 
def dashboard():
    return render_template('/admin/dashboard.html',session = session)


