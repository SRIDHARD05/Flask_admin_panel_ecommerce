from flask import Blueprint, request, jsonify, render_template
import base64

bp = Blueprint("errors", __name__, url_prefix="/errors")


@bp.route('/404')
def error_404():
    return render_template('components/error/error_404.html')


@bp.route('/500')
def error_500():
    return render_template('components/error/error_500.html')

