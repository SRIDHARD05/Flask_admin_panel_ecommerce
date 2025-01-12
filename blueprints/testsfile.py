from flask import Flask, redirect, url_for, request, render_template, session, jsonify,Blueprint

bp = Blueprint("testsfile", __name__, url_prefix="/test")

@bp.route('/', methods=['POST'])  
def dashboard():
    data = request.get_json()
    data1 = 'paragraph1'
    data2 = 'paragraph2'
    data3 = 'paragraph3'
    data4 = 'paragraph4'
    data5 = 'paragraph5'

    return jsonify({
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data' : data
    })


@bp.route('/tabs')
def tabs():
    data  = 'This is a sample Data'
    return render_template("designs/tabs.html",data = data)