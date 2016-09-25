from flask import Blueprint, session, request, redirect, url_for, render_template, flash, abort
from truckz import get_database

mod = Blueprint('journeys', __name__)

def get_owner_id(login_name):
    db = get_database()
    rows = db.execute(\
        'select owner_id from owners where owner_auth_username=:username', {'username': login_name}\
    )
    row = rows.fetchone()
    return row[0]

def get_customer_id(login_name):
    db = get_database()
    rows = db.execute(\
        'select customer_id from customers where customer_auth_username=:username', {'username': login_name}\
    )
    row = rows.fetchone()
    return row[0]

@mod.route('/journeys')
def journeys():
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please login again')

    db = get_database()

    if session.get('user_type') == 'owner':
        rows = db.execute(\
            'select * from journey_plan where  journey_provider_id=:owner_id',\
            {'owner_id': get_owner_id(session.get('user_name'))}\
        )
    elif session.get('user_type') == 'customer':
        rows = db.execute(\
            'select * from journey_plan where journey_recipient_id=:cust_id',\
            {'cust_id': get_customer_id(session.get('user_name'))}\
        )
    else:
        rows = db.execute('select * form journey_plan')

    journeys = rows.fetchall()
    return render_template('journeys/journeys.html', journeys = journeys)

@mod.route('/journeys/edit')
def edit_journeys():
    return render_template('journeys/add_journeys.html')

'''
This method should be accessible only to owners.
For the sake of security, we check if the session owner
is logged in and is an owner and not a customer or otherwise.
'''
@mod.route('/journeys/add', methods=['POST', 'GET'])
def add_journeys():
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please login again')
    else:
        if not session.get('user_type') == 'owner':
            abort(401, message='Access denied')
        else:
            db = get_database()
            db.execute(\
                'insert into journey_plan(\
                    journey_recipient_id,\
                    journey_provider_id,\
                    journey_pickup_date,\
                    journey_dropoff_date,\
                    journey_rate\
                ) values(?,?,?,?,?)',[\
                    request.form['recipient_id'],\
                    request.form['pickup_date'],\
                    request.form['dropoff_date'],\
                    request.form['rate']\
                ]\
            )
            db.commit()
            flash('Your journey was successfully added')
            return redirect(url_for('journeys.journeys'))
