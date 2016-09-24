from .auth import login
from truckz import get_database
from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort

mod = Blueprint('dashboard', __name__)

@mod.route('/')
def index():
    return render_template('dashboard.html')

@mod.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return login('customer')

@mod.route('/dashboard/profile/', methods=['POST', 'GET'])
def profile_view():
    auth_name = session.get('user_name')
    db = get_database()
    cur = db.execute('select * from customers where customer_auth_username=:auth_user', {"auth_user": auth_name})
    details = cur.fetchone()
    return render_template('profile/profile.html', details = details)

@mod.route('/dashboard/profile/edit', methods=['POST', 'GET'])
def profile_edit():
    return render_template('profile/edit_profile.html')

@mod.route('/dashboard/profile/update', methods=['POST', 'GET'])
def profile_update():
    if not session.get('logged_in'):
        abort(401, message="Session expired. Please login again")
    db = get_database()
    db.execute('update customers set customer_name=?, customer_email=?, customer_contact=?, customer_address=? where customer_auth_username=?',
               [request.form['name'], request.form['email'], request.form['contact'], request.form['address'], session.get('user_name')])
    db.commit()
    flash('Profile updated')
    return redirect(url_for('dashboard.profile_view'))
