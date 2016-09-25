from flask import Blueprint, request, render_template, url_for, redirect, session, abort, flash
from truckz import get_database

mod = Blueprint('trucks', __name__)

@mod.route('/trucks', defaults={'path':''})
@mod.route('/trucks/<path:path>')
def show_trucks(path):
    db = get_database()
    if path == '':
        rows = db.execute('select * from trucks')
    else:
        rows = db.execute('select * from trucks where truck_model =?', path)
    trucks = rows.fetchall()
    return render_template('trucks/trucks.html', trucks=trucks)

@mod.route('/trucks/edit', methods=['POST', 'GET'])
def edit_trucks():
    return render_template('trucks/add_trucks.html')

@mod.route('/trucks/add', methods=['POST', 'GET'])
def add_trucks():
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please Login again')
    db = get_database()
    db.execute(\
        'insert into trucks(\
            truck_model,\
            truck_weight,\
            truck_volume,\
            truck_current_location,\
            truck_registration_number\
        ) values(?,?,?,?,?)',[\
            request.form['model'],\
            request.form['weight'],\
            request.form['volume'],\
            request.form['location'],\
            request.form['regno']\
        ]\
    )
    db.commit()
    flash('Model ' + request.form['model'] + ' added Successfully')
    return redirect(url_for('trucks.show_trucks'))
