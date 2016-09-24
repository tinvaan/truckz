from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from truckz import get_database, init_database

mod = Blueprint('auth', __name__)

@mod.route('/login', methods=['POST', 'GET'])
def login(user):
    error = None
    db = get_database()
    init_database()

    if request.method == 'POST':
        if user == 'owner':
            rows = db.execute("select owner_auth_username and owner_auth_password from owners where owner_auth_username=:auth_user and owner_auth_password=:auth_pass", {"auth_user": request.form['username'], "auth_pass": request.form['password']})
        elif user == 'customer':
            rows = db.execute("select customer_auth_username, customer_auth_password from customers where customer_auth_username=:auth_user and customer_auth_password=:auth_pass", {"auth_user": request.form['username'], "auth_pass": request.form['password']})
        else:
            abort(404, message={'User not found'})

        row = rows.fetchone()
        if not row is None:
            if row['customer_auth_username'] == request.form['username'] and row['customer_auth_password'] == request.form['password']:
                session['logged_in'] = True
                session['user_name'] = request.form['username']
                flash('Login successful')
                return redirect(url_for('dashboard.index'))
            else:
                error='Username or password not found in database'
        else:
            error = 'Username or password not found in database'
    return render_template('login.html', error=error)

"""
An alternative method that doesn't access the database
and checks only against app.config keys.
Can be used to partially debug your app even without a database
"""
'''
@mod.route('/simple_login', methods=['POST', 'GET'])
def simple_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('Successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
'''

@mod.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out')
    return redirect(url_for('dashboard.index'))
