from flask import Blueprint, session, request, redirect, url_for, render_template, flash, abort
from truckz import get_database

mod = Blueprint('bookings', __name__)

@mod.route('/bookings')
def bookings():
    error = None
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please login again')
    db = get_database()

    customers = db.execute("select customer_id from customers where customer_auth_username=:booking_owner_name", {"booking_owner_name":session.get('user_name')})
    customer_row = customers.fetchone()

    if customer_row is not None:
        customer_id = customer_row['customer_id']
        customer_bookings = db.execute("select * from bookings where booking_owner_id=:c_id", {"c_id":customer_id})
        c_bookings = customer_bookings.fetchall()
        return render_template('bookings/bookings.html', bookings=c_bookings, error=error)
    else:
        error = 'You have made no bookings so far'
        return render_template('bookings/bookings.html', error=error)

@mod.route('/bookings/all')
def all_bookings():
    db = get_database()
    rows = db.execute('select * from bookings')
    a_bookings = rows.fetchall()
    return render_template('bookings/bookings.html', bookings = a_bookings)

@mod.route('/bookings/edit')
def edit_bookings():
    return render_template('bookings/add_bookings.html')

@mod.route('/bookings/add', methods=['POST', 'GET'])
def add_bookings():
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please login again')
    else:
        if not session.get('user_type') == 'customer':
            abort(401, message='Access denied')
        else:
            db = get_database()
            db.execute('insert into bookings(booking_source_stop, booking_destination_stop, booking_requested_pickup_date, booking_requested_dropoff_date, booking_shipment) values(?,?,?,?,?)',
                    [ request.form['source_stop'], request.form['dest_stop'], request.form['req_pickup'], request.form['req_dropoff'], request.form['shipments'] ])
            db.commit()
            flash('Your booking request has been lodged')
            return redirect(url_for('bookings.bookings'))
