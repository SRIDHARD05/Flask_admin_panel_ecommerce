from flask import Blueprint, request, jsonify, render_template
from src.SeoReport import SeoReport
import logging

bp = Blueprint("shopify_seo", __name__, url_prefix="/shopify_seo")

@bp.route('/')
def dashboard():
    return render_template('components/shopify/reports/dashboard.html')

@bp.route('/report/generate', methods=['GET'])
def generate_report():
    try:
        domain_name = request.args.get('s')
        if not domain_name:
            return jsonify({'status': 'failed', 'message': 'Domain name is required'}), 400

        report = SeoReport.generate_report(domain_name)
        return jsonify(report), (200 if report.get('status') == 'success' else 500)

    except Exception as e:
        logging.exception("Error occurred while generating the report")
        return jsonify({'status': 'failed', 'message': str(e)}), 500

"""
 add and update the designs add the title and input with btn with a clean and professional design: and also design my code "{% extends '__master.html' %}

{% block content %}
<div class="container" style="max-width: 1200px; margin: auto; padding: 20px;">
    <input type="url" name="domain_name" placeholder="Enter domain name" required>
    <div id="generate_report" class="btn btn-primary btn-rounded text-center">Submit</div>
</div>

{% endblock %}" 
"""