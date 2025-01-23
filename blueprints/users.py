from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash,session
import base64
from src.User import User
from src.Session import Session
from src import hash_data

bp = Blueprint("users", __name__, url_prefix="/users")


# TODO: Reset Password Templates    
@bp.route('/reset_password')
def reset_password():
    return render_template('reset_password.html')



@bp.route("/register", methods=['POST'])
def register():
    # TODO: Create a Default User Save Collecitons Records
    if 'name' in request.form and 'password' in request.form and 'repeatpassword' in request.form and 'email' in request.form:
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']
        repeat_password = request.form['repeatpassword']
        if password == repeat_password :
            try:
                user_data = User.register(username, password, password, email)
                session['authenticated'] = True
                session['username'] = username
                session['email'] = email
                session['sessid'] = user_data['uuid']
                session['user_id'] = hash_data(user_data['uuid'])
                session['role'] = user_data['role']
                if session['authenticated'] :
                    return redirect(url_for('dashboard.index')) 

            except Exception as e:
                print(str(e))
                return redirect(url_for('signup'))

            except Exception as e:
                print(str(e))
                return redirect(url_for('signup'))
        else:
            return redirect(url_for('signup'))
        
    else:
        return redirect(url_for('signup'))



@bp.route("/deauth")
def deauth():
   if session.get('authenticated'): #TODO: Need more validattion like login expiry
        #Remove / invalidate session from database
        # session['authenticated'] = False
        session.clear()
        return redirect(url_for('dashboard.index')) 
   else:
        return redirect(url_for('signin'))
      

@bp.route("/login", methods=['POST'])
def authenticate():
    if session.get('authenticated'):  # TODO: Need more validation like login expiry and session expiry
        sess = Session(session['sessid'])
        if sess.is_valid():
            if session.get('role') == 'admin':
                return redirect(url_for('admin.dashboard'))  
            else:
                return redirect(url_for('dashboard.index'))  
        else:
            session['authenticated'] = False
            sess.collection.active = False
            return redirect(url_for('signin'))  

    else:
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            try:
                sess_data = User.login(email, password)
                print(sess_data)
                
                session['authenticated'] = True
                session['email'] = email
                session['sessid'] = sess_data['sess_id']
                session['type'] = 'web'
                session['role'] = sess_data['role']
                session['user_id'] = hash_data(sess_data['user_id'])
                session['credits'] = sess_data['credits']
                session['username'] = sess_data['username']
                
                if session['role'] == 'admin':
                    return redirect(url_for('admin.dashboard'))  
                else:
                    return redirect(url_for('dashboard.index')) 
                
            except Exception as e:
                print(str(e))
                return redirect(url_for('signin')) 
        else:
            return redirect(url_for('signin'))
