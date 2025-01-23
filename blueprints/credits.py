from flask import Blueprint, request, jsonify, render_template, session
import base64
from src.User import User

bp = Blueprint("credits", __name__, url_prefix="/credits")

@bp.route('/', methods=['GET'])
def dashboard():
    return render_template('credits.html',data = session)

@bp.route('/get', methods=['GET'])
def get():
    get_credits = User.get_credits()
    return jsonify({
        'message' : 'credits retrieved successfully',
        'credits' : get_credits
    }),200


# TODO: For Payments Processing...
@bp.route('/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        credits = data.get('credits')

        if credits is None:
            return jsonify({'message': 'Credits data is required'}), 400

        updated_credits = User.add_credits(credits)

        if updated_credits:
            return jsonify({
                'message': 'Credits updated successfully',
                'credits': credits
            }), 200
        elif updated_credits is False: 
            return jsonify({
                'message': 'Failed to update credits. Please try again.'
            }), 400
        else: 
            return jsonify({
                'message': 'User not authenticated. Please sign in.'
            }), 401

    except Exception as e:
        return jsonify({
            'message': 'An error occurred while updating credits',
            'error': str(e)
        }), 500


@bp.route('/update', methods=['POST'])
def update():
    try:
        data = request.get_json()

        if not data or 'credits' not in data:
            return jsonify({'message': 'Credits data is required'}), 400

        try:
            credits = int(data['credits'])  
        except ValueError:
            return jsonify({'message': 'Credits must be a valid integer'}), 400

        updated_credits = User.update_credits(credits)

        if updated_credits is not None:
            return jsonify({
                'message': 'Credits updated successfully',
                'credits': updated_credits
            }), 200
        elif updated_credits is False: 
            return jsonify({
                'message': 'Failed to update credits. Please try again.'
            }), 400
        else:
            return jsonify({
                'message': 'User not authenticated. Please sign in.'
            }), 401

    except Exception as e:
        print(f"Error in /update route: {e}") 
        return jsonify({
            'message': 'An error occurred while updating credits',
            'error': str(e)
        }), 500
