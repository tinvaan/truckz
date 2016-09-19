from truckz import app
from truckz.app_db import get_database, init_database
from flask import render_template, url_for, redirect, flash, session, request, abort, jsonify

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return redirect(url_for('index'))

@app.route('/dashboard/profile/', methods=['POST', 'GET'])
def profile_view():
    return render_template('profile.html')

@app.route('/dashboard/profile/edit', methods=['POST', 'GET'])
def profile_edit():
    return render_template('edit_profile.html')

@app.route('/login', methods=['POST', 'GET'])
def login(user):
    error = None
    db = get_database()
    init_database()

    if request.method == 'POST':
        if user == 'owner':
            rows = db.execute('select owner_auth_username and owner_auth_password from owners where owner_auth_username=? and owner_auth_password=?',
                            [request.form['username'], request.form['password']])
        elif user == 'customer':
            rows = db.execute('select customer_auth_username, customer_auth_password from customers where customer_auth_username=? and customer_auth_password=?',
                              [request.form['Username'], request.form['password']])
        else:
            abort(404, message={'User not found'})
        if rows > 0:
            session['logged_in'] = True
            flash('Login successful')
            return redirect(url_for('index'))
        else:
            error='Username or password not found in database'
    return render_template('login.html', error=error)

"""
An alternative method that doesn't access the database
and checks only against app.config keys
"""
@app.route('/simple_login', methods=['POST', 'GET'])
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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out')
    return redirect(url_for('index'))

@app.route('/trucks', defaults={'path':''})
@app.route('/trucks/<path:path>')
def show_trucks(path):
    db = get_database()
    init_database()
    if path == '':
        rows = db.execute('select * from trucks')
    else:
        rows = db.execute('select * from trucks where truck_id =?', path)
    trucks = rows.fetchall()
    return render_template('trucks.html', trucks=trucks)

@app.route('/trucks/add', methods=['POST', 'GET'])
def add_trucks():
    return render_template('add_trucks.html')

@app.route('/bookings', methods=['POST', 'GET'])
def bookings():
    return render_template('bookings.html')

@app.route('/bookings/add', methods=['POST', 'GET'])
def add_bookings():
    return render_template('add_bookings.html')

@app.route('/journeys', methods=['POST', 'GET'])
def journeys():
    return render_template('journeys.html')

@app.route('/journeys/add', methods=['POST', 'GET'])
def add_journeys():
    return render_template('add_journeys.html')

@app.route('/owners', defaults={'path':''}, methods=['POST', 'GET'])
@app.route('/owners/<path:path>')
def show_owners(path):
    if not session.get('logged_in'):
        return simple_login()
    else:
        db = get_database()
        init_database()
        if path == '':
            rows = db.execute('select * from owners')
        elif path == 'login':
            return simple_login()
        else:
            rows = db.execute('select * from owners where owner_id=?', path)
        owners = rows.fetchall()
        return jsonify(owners)

@app.route('/customers', defaults={'path':''}, methods=['POST', 'GET'])
@app.route('/customers/<path:path>')
def show_customers(path):
    if not session.get('logged_in'):
        return simple_login()
    else:
        db = get_database()
        init_database()
        if path == '':
            rows = db.execute('select * from customers')
        elif path == 'login':
            return simple_login()
        else:
            rows = db.execute('select * from customers where customers_id=?', path)
        customers = rows.fetchall()
        return jsonify(customers)
