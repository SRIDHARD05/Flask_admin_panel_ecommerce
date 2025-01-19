from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
import base64
from src.Save import Save

bp = Blueprint("save_posts", __name__, url_prefix="/save")

@bp.route('/')
def dashboard():
    if "authenticated" in session :
        posts_collections = Save.get_saved_posts_collections(session['email'])
        return render_template('history.html', saved_posts=posts_collections)
    else:
        return redirect(url_for('signin'))



@bp.route('/posts/saved_post/<collection_name>', methods=['GET'])
def saved_posts(collection_name):
    if "authenticated" in session :
        try:
            if 'email' not in session:
                return redirect(url_for('users.sigin'))

            email = session['email']
            posts = Save.get_saved_posts(email, collection_name)
            data = [post['product_id'] for post in posts]
            # TODO: Hide the products ID instead of use Hashing
            return render_template("components/save/post_views.html", posts=data,collection_name = collection_name)

        except Exception as e:
            return redirect(url_for('save_posts.dashboard', _external=True))
    else:
        return redirect(url_for('signin'))




@bp.route('/posts/save', methods=['POST'])
def user_save():
    if "authenticated" in session :
        jsonData = request.get_json()
        email = session['email']
        collection_name = jsonData['collection_id']  
        product_id = jsonData['product_id']
        media_type = 'sample'  
        product_id_hash = "Hashed Product ID"
        try:
            save_posts = Save.save_posts(email, collection_name, media_type, product_id, product_id_hash)
            print(save_posts)
            return jsonify({
                "status": 200,
                "message": "Data Saved Successfully"
            }), 200
        
        except Exception as e:
            return jsonify({
                "status": 400,
                "message": str(e),
            }), 400
    else:
        return redirect(url_for('signin'))



@bp.route('/collection/create', methods=['POST'])
def create_collections():
    if "authenticated" in session :
        jsonData = request.get_json()
        collection_name = jsonData.get('name')  
        email = session.get('email')  
        print(collection_name)
        if not email:
            return jsonify({
                "status": 400,
                "message": "User email not found in session."
            }), 400

        try:
            result = Save.create_collections(email, collection_name)
            if result["success"]:
                return jsonify({
                    "status": 200,
                    "message": result["message"]
                }), 200
            else:
                return jsonify({
                    "status": 400,
                    "message": result["message"]
                }), 400
        except Exception as e:
            return jsonify({
                "status": 500,
                "message": str(e)
            }), 500
    else:
        return redirect(url_for('signin'))


@bp.route('/collection/create/modal')
def create_collection_template():
    return render_template('components/save/create.html')

@bp.route('/collection/show', methods=['GET'])
def save_collections():
    if "authenticated" in session :
        try:
            email = session['email']
            posts_collections = Save.get_saved_posts_collections(email)
            if not posts_collections:
                return render_template('components/save/collections_show.html', data=[], message="No collections found")

            return render_template('components/save/collections_show.html', data=posts_collections)

        except Exception as e:
            return jsonify({
                "status": 400,
                "message": str(e),
            }), 400
    else:
        return redirect(url_for('signin'))



@bp.route('/collection/delete', methods=['POST'])
def delete_collection():
    if "authenticated" in session :
        jsonData = request.get_json()
        collection_name = jsonData.get('name')
        email = session.get('email')

        if not email:
            return jsonify({
                "status": 400,
                "message": "User email not found in session."
            }), 400

        try:
            result = Save.delete_collection(email, collection_name)

            if result["success"]:
                return jsonify({
                    "status": 200,
                    "message": result["message"]
                }), 200
            else:
                return jsonify({
                    "status": 400,
                    "message": result["message"]
                }), 400
        except Exception as e:
            return jsonify({
                "status": 500,
                "message": str(e)
            }), 500
    else:
        return redirect(url_for('signin'))



@bp.route('/post/delete', methods=['POST']) 
def delete_post():
    if "authenticated" in session :
        try:
            data = request.get_json()
            post_name = data.get('post_name')
            collection_name = data.get('collection_name')
            email = session.get('email')

            if not post_name or not collection_name or not email:
                return jsonify({"status": 400, "message": "Missing required data."}), 400

            result = Save.delete_post(email, collection_name, post_name)
            return jsonify(result), result["status"]
        except Exception as e:
            return jsonify({"status": 500, "message": "An internal error occurred. Please try again later."}), 500
    else:
        return redirect(url_for('signin'))
