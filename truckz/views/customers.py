from .auth import login
from truckz import get_database
from flask import Blueprint, session, request, redirect, jsonify

mod = Blueprint('customers', __name__)

@mod.route('/customers', defaults={'path':''}, methods=['POST', 'GET'])
@mod.route('/customers/<path:path>')
def show_customers(path):
    if not session.get('logged_in'):
        return login('customer')
    else:
        db = get_database()
        if path == '':
            rows = db.execute('select * from customers')
        elif path == 'login':
            return login('customer')
        else:
            rows = db.execute('select * from customers where customers_id=?', path)
        customers = rows.fetchall()
        return jsonify(customers)
