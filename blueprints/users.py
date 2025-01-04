from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
import base64

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


@bp.route('/login', methods=['POST'])
def login():
    name = request.form['email']
    password = request.form['password']

    print(f"Name ;; {name}")
    if name and password:
        # TODO: Implement user email and password validations with db connections
        return redirect(url_for('dashboard.index'))
    else:
        return redirect(url_for('users.signin'))


@bp.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form.get('email')
    password = request.form.get('password')
    repeat_password = request.form.get('repeat_password')
    email = request.form.get('email')
    is_checked = request.form.get('is_checked')  # Get checkbox value
    
    print(f'is Checked =>', is_checked)
    
    # Validation for required fields
    if not is_checked:
        flash('You must agree to the Terms and Conditions', 'error')  # Flash error message
        return redirect(url_for('users.signup'))
    
    if not name or not password or not repeat_password or not email:
        flash('All fields are required', 'error')  # Flash error message
        return redirect(url_for('users.signup'))
    
    if password != repeat_password:
        flash('Passwords do not match', 'error')  # Flash error message
        return redirect(url_for('users.signup'))

    # If everything is correct
    flash('Signup successful! Redirecting...', 'success')  # Flash success message
    return redirect(url_for('dashboard.index'))  # Redirect to dashboard
