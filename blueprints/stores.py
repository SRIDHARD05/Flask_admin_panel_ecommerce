from flask import Flask, request, jsonify, render_template, Blueprint, session
from bson import ObjectId, errors 
from src import login_required, user_required, admin_required 
from src.Stores import Stores
from urllib.parse import unquote
from bson import ObjectId

bp = Blueprint("stores", __name__, url_prefix="/stores")


@bp.route("/view/insights", methods=['GET'])  
@user_required
def store_insights_view():
    store_url = request.args.get('store_url')
    if store_url:
        decoded_store_url = unquote(store_url)
        store_insights_data = Stores.view_insights(decoded_store_url)

        return render_template('components/stores/reports/dashboard.html', data=store_insights_data)


@bp.route("/shopify/all",methods=['GET'])
@user_required
def dashboard():
    title = "Shopify Stores"
    data = Stores.store_view()
    return render_template('components/stores/dashboard.html',stores = data['data'],title = title)


@bp.route("/save",methods=['GET'])
@admin_required
def save_store():
    return render_template('components/stores/save.html')


@bp.route("/save", methods=['POST'])
@admin_required
def save_store_db():
    html_content = request.form.get('stores-data', '')

    if not html_content.strip():
        return jsonify({
            'status': '400',
            'message': 'HTML content is empty. Please provide valid data.'
        }), 400
    result = Stores.store_save(html_content)
    if result['status'] == 200 :
        return jsonify({
            'message' : 'Data Stored successfully',
            'status' : 200
        }),200
    else :
        return jsonify(result),500


@bp.route("/best-stores/save",methods=['GET'])
@admin_required
def save_template():
    return render_template('components/stores/best_stores/save.html')


@bp.route("/best-stores/save", methods=['POST'])
@admin_required
def save_best_store():
    html_content = request.form.get('stores-data', '')
    store_type = request.form.get('store_type', '')  
    
    if not html_content.strip():
        return jsonify({
            'status': '400',
            'message': 'HTML content is empty. Please provide valid data.'
        }), 400

    email = session['email']
    result = Stores.best_stores_save(store_type, email, html_content)

    if(result['status'] == '200'):
        return result
    else:
        return result


@bp.route("/best-stores/<string:store_type>",methods=['GET'])
@user_required
def best_stores(store_type):
    data = {}
    
    if store_type == 'top-100-shopify-stores-2025': 
        data['title'] = 'Top 100 Shopify Stores 2025'
        data['store_data'] = Stores.best_stores_view('shopify')
        
    if store_type == 'top-stores-&-sellers-on-aliexpress-2025': 
        data['title'] = 'Top Stores & Sellers on Aliexpress 2025'
        data['store_data'] = Stores.best_stores_view('aliexpress') 

    if store_type == 'biggest-amazon-sellers-2025-top-100': 
        data['title'] = 'Biggest Amazon Sellers 2025 - Top 100'
        data['store_data'] = Stores.best_stores_view('amazon')

    if store_type == 'top-100-lazada-stores-2025': 
        data['title'] = 'Top 100 Lazada Stores 2025'
        data['store_data'] = Stores.best_stores_view('lazada')

    if store_type == 'top-100-shopee-stores-2025': 
        data['title'] = 'Top 100 Shopee Stores 2025'
        data['store_data'] = Stores.best_stores_view('shope')

    if store_type == 'top-100-wish-stores-2025': 
        data['title'] = 'Top 100 Wish Stores 2025'
        data['store_data'] = Stores.best_stores_view('wish')

    if store_type == 'top-100-shopify-stores-in-australia-2025': 
        data['title'] = 'Top 100 Shopify Stores in Australia 2025'
        data['store_data'] = Stores.best_stores_view('austrilia')

    if store_type == 'top-100-shopify-stores-in-brazil-2025': 
        data['title'] = 'Top 100 Shopify Stores in Brazil 2025'
        data['store_data'] = Stores.best_stores_view('brazil')

    if store_type == 'top-100-shopify-stores-in-canada-2025': 
        data['title'] = 'Top 100 Shopify Stores in Canada 2025'
        data['store_data'] = Stores.best_stores_view('canada')

    if store_type == 'top-100-shopify-stores-in-france-2025': 
        data['title'] = 'Top 100 Shopify Stores in France 2025'
        data['store_data'] = Stores.best_stores_view('france') 

    if store_type == 'top-100-shopify-stores-in-united-kingdom-2025': 
        data['title'] = 'Top 100 Shopify Stores in United Kingdom 2025'
        data['store_data'] = Stores.best_stores_view('uk')

    if store_type == 'top-100-shopify-stores-in-united-states-2025': 
        data['title'] = 'Top 100 Shopify Stores in United States 2025'
        data['store_data'] = Stores.best_stores_view('us')

    if store_type == 'top-100-shopify-beauty-&-health-stores-2025': 
        data['title'] = 'Top 100 Shopify Beauty & Health Stores 2025'
        data['store_data'] = Stores.best_stores_view('beauty')

    if store_type == 'top-100-shopify-clothing,-shoes-&-jewelry-stores-2025': 
        data['title'] = 'Top 100 Shopify Clothing, Shoes & Jewelry Stores 2025'
        data['store_data'] = Stores.best_stores_view('clothing')

    if store_type == 'top-100-shopify-consumer-electronics-stores-2025': 
        data['title'] = 'Top 100 Shopify Consumer Electronics Stores 2025'
        data['store_data'] = Stores.best_stores_view('consumer')

    if store_type == 'top-100-shopify-home-improvement-stores-2025': 
        data['title'] = 'Top 100 Shopify Home Improvement Stores 2025'
        data['store_data'] = Stores.best_stores_view('home_improvement') 

    if store_type == 'top-100-shopify-home-&-garden-&-kitchen-stores-2025': 
        data['title'] = 'Top 100 Shopify Home & Garden & Kitchen Stores 2025'
        data['store_data'] = Stores.best_stores_view('home')

    if store_type == 'top-100-shopify-office-&-school-supplies-stores-2025': 
        data['title'] = 'Top 100 Shopify Office & School Supplies Stores 2025'
        data['store_data'] = Stores.best_stores_view('office')

    if store_type == 'top-100-shopify-sports-&-entertainment-stores-2025': 
        data['title'] = 'Top 100 Shopify Sports & Entertainment Stores 2025'
        data['store_data'] = Stores.best_stores_view('sports')

    if store_type == 'top-100-shopify-toys-&-game-stores-2025': 
        data['title'] = 'Top 100 Shopify Toys & game Stores 2025'
        data['store_data'] = Stores.best_stores_view('toyes')

    return render_template('components/stores/best_stores/view.html',data = data)

            






