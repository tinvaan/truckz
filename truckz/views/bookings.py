from flask import Blueprint, session, request, redirect, url_for, render_template, flash, abort
from truckz import get_database

mod = Blueprint('bookings', __name__)

@mod.route('/bookings')
def bookings():
    if not session.get('logged_in'):
        abort(401, message='Session expired. Please login again')
    db = get_database()

    cust = db.execute("select customer_id from customers where customer_auth_username=:booking_owner_name", {"booking_owner_name":session.get('user_name')})
    row = cust.fetchone()
    cust_id = row[0]

    cust_bookings = db.execute("select * from bookings where booking_owner_id=:customer_id", {"customer_id":cust_id})
    c_bookings = cust_bookings.fetchall()
    return render_template('bookings.html', bookings = c_bookings)

@mod.route('/bookings/edit')
def edit_bookings():
    return render_template('add_bookings.html')

@mod.route('/bookings/add', methods=['POST', 'GET'])
def add_bookings():
    db = get_database()
    db.execute('insert into bookings(booking_source_stop, booking_destination_stop, booking_requested_pickup_date, booking_requested_dropoff_date, booking_shipment) values(?,?,?,?,?)',
               [ request.form['source_stop'], request.form['dest_stop'], request.form['req_pickup'], request.form['req_dropoff'], request.form['shipments'] ])
    db.commit()
    flash('Your booking request has been lodged')
    return redirect(url_for('bookings.bookings'))
