from flask import Blueprint, request, jsonify, render_template
import base64
bp = Blueprint("sidebar", __name__, url_prefix="/sidebar")



'''
For Tab 1 -> Tab 1 Nav Bar Item
'''
@bp.route('/search/tab1/navbar')
def nav_bar():
    return render_template('components/search_filters_templates/tab1/nav_bar.html')

@bp.route('/search/tab1/dates')
def products_nav_bar():
    return render_template('components/search_filters_templates/tab1/dates_nav_bar.html')

@bp.route('/search/tab1/reactions')
def reactions_nav_bar():
    return render_template('components/search_filters_templates/tab1/reactions_nav_bar.html')

@bp.route('/search/tab1/target_audience')
def target_audience_nav_bar():
    return render_template('components/search_filters_templates/tab1/target_audience_nav_bar.html')
    