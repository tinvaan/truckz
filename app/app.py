"""
Contains the general setup/config of the application.
"""

import os, sqlite3
from flask import Flask, Blueprint, g
from flask_restful import Api

from truckzio.app.trucks import Trucks
from truckzio.app.owners import Owners
from truckzio.app.customers import Customers

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'app.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

api_bp = Blueprint('api', __name__)
api = Api(app)

api.add_resource(Trucks, 'Trucks', 'Trucks/<str: id>')
api.add_resource(Owners, '/Owners', '/Owners/<str: id>')
api.add_resource(Customers, '/Customers', '/Customers/<str: id>')

def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection

def get_database():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_database():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_database():
    db = get_database()
    with app.open_resource('schemas.sql', mode='r') as dbFile:
        db.cursor().executescript(dbFile.read())
    db.commit()

app.register_blueprint(api_bp)
