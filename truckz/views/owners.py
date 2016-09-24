from .auth import login
from truckz import get_database
from flask import Blueprint, request, session, jsonify

mod = Blueprint('owners', __name__)

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
