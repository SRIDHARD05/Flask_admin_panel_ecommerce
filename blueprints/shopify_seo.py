from flask import Blueprint, request, jsonify, render_template
import base64
import json
from src.SeoReport import SeoReport
from datetime import datetime

bp = Blueprint("shopify_seo", __name__, url_prefix="/shopify_seo")

# TODO: Create and connect the Amazon S3 Storage
# amazon_s3_connection = AmazonS3.get_connection()

@bp.route('/')
def dashboard():
    return render_template('components/shopify/reports/dashboard.html')


@bp.route('/report/generate/s=?<domain_name>', methods=['GET'])
def generate_report(domain_name):
    report = SeoReport.generate_report(domain_name)
    if 'status' in report and report['status'] == 'success' and 'data' in report and report['data'] != None :
        return jsonify({
            'message' : 'file upload success',
            'status' : 'success',
            'data' : report['data']
        }),200

    else:
        return jsonify({
            'status': 'failed',
            'message': f"Error executing command for {url}",
            'error': str(e)
        }), 500