from .auth import login
from truckz import get_database
from flask import Blueprint, request, session, jsonify

mod = Blueprint('owners', __name__)

def get_owner_id():
    db = get_database()
    cur = db.execute('select * from owners where owner_auth_username=?', [session.get('user_name')])
    row = cur.fetchone()
    return row['owner_id']

'''
Returns the id's of the trucks owned
by the logged in user
To access the trucks later,
    for truck in get_trucks_owned():
        truck['truck_id']
'''
def get_trucks_owned():
    db = get_database()
    cur = db.execute('select owner_trucks from owners where owner_id=?', [get_owner_id()])
    rows = cur.fetchall()
    return rows

@mod.route('/owners', defaults={'path':''}, methods=['POST', 'GET'])
@mod.route('/owners/<path:path>')
def show_owners(path):
    if not session.get('logged_in'):
        return login('owner')
    else:
        db = get_database()
        if path == '':
            rows = db.execute('select * from owners')
        elif path == 'login':
            return login('owner')
        else:
            rows = db.execute('select * from owners where owner_id=?', path)
        owners = rows.fetchall()
        return jsonify(owners)
