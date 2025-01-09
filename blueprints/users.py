from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash,session
import base64
from src.User import User
bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route('/signin')
def signin():
    return render_template('sign_in.html')


@bp.route('/signup')
def signup():
    return render_template('sign_up.html')

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
                uid = User.register(username, password, password, email)
                session['authenticated'] = True
                session['username'] = username
                session['email'] = email
                session['sessid'] = uid
                if session['authenticated'] :
                    print(uid)
                    return redirect(url_for('dashboard.index')) 

            except Exception as e:
                print(str(e))
                return redirect(url_for('users.signup'))

            except Exception as e:
                print(str(e))
                return redirect(url_for('users.signup'))
        else:
            return redirect(url_for('users.signup'))
        
    else:
        return redirect(url_for('users.signup'))



@bp.route("/deauth")
def deauth():
   if session.get('authenticated'): #TODO: Need more validattion like login expiry
        #Remove / invalidate session from database
        session['authenticated'] = False
        return redirect(url_for('dashboard.index')) 
   else:
        return redirect(url_for('users.signin'))
      

@bp.route("/login", methods=['POST'])
def authenticate():
    if session.get('authenticated'): #TODO: Need more validattion like login expiry, and session expiry
        print(session)
        sess = Session(session['sessid'])
        if sess.is_valid():
            return redirect(url_for('dashboard.index')) 
        else:
            session['authenticated'] = False
            sess.collection.active = False
            return redirect(url_for('users.signin'))

    else:
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            try:
                sessid = User.login(email, password)
                session['authenticated'] = True
                session['email'] = email
                session['sessid'] = sessid
                session['type'] = 'web'
                
                if 'redirect' in request.form and request.form['redirect'] == 'true':
                    return redirect(url_for('dashboard.index'))
                else:
                    return redirect(url_for('dashboard.index'))
                
            except Exception as e:
                print(str(e))
                return redirect(url_for('users.signin'))
        else:
            return redirect(url_for('users.signin'))