from flask import Blueprint, request, jsonify, render_template
import base64
from src.Load_data import Load_data
bp = Blueprint("sidebar", __name__, url_prefix="/sidebar")



@bp.route('/search/navbar')
def nav_bar():
    return render_template('components/search_filters_templates/nav_bar.html')


@bp.route('/search/dates')
def products_nav_bar():
    return render_template('components/search_filters_templates/dates_nav_bar.html')


@bp.route('/search/reactions')
def reactions_nav_bar():
    return render_template('components/search_filters_templates/reactions_nav_bar.html')


@bp.route('/search/target_audience')
def target_audience_nav_bar():
    return render_template('components/search_filters_templates/target_audience_nav_bar.html')
    