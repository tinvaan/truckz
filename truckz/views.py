from truckz import app
from truckz.app_db import get_database, init_database
from flask import render_template, url_for, redirect, flash, session, request, abort, jsonify

@app.route('/')
def index():
    return render_template('index.html')

def login(user):
    error = None
    db = get_database()
    init_database()

    if request.method == 'POST':
        if user == 'owner':
            rows = db.execute('select owner_auth_username and owner_auth_password from owners where owner_auth_username=? and owner_auth_password=?',
                            [request.form['username'], request.form['password']])
        elif user == 'customer':
            rows = db.execute('select customer_auth_username, customer_auth_password from customers where customer_auth_username=(?) and customer_auth_password=(?)',
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
        rows = db.execute('select * from trucks where truck_id =(?)', path)
    trucks = rows.fetchall()
    return jsonify(trucks)

@app.route('/owners', defaults={'path':''}, methods=['POST', 'GET'])
@app.route('/owners/<path:path>')
def show_owners(path):
    db = get_database()
    init_database()
    if path == '':
        rows = db.execute('select * from owners')
    elif path == 'login':
        return login('owner')
    else:
        rows = db.execute('select * from owners where owner_id=(?)', path)
    owners = rows.fetchall()
    return jsonify(owners)

@app.route('/customers', defaults={'path':''}, methods=['POST', 'GET'])
@app.route('/customers/<path:path>')
def show_customers(path):
    db = get_database()
    init_database()
    if path == '':
        rows = db.execute('select * from customers')
    elif path == 'login':
        return login('customer')
    else:
        rows = db.execute('select * from customers where customers_id=(?)', path)
    customers = rows.fetchall()
    return jsonify(customers)
