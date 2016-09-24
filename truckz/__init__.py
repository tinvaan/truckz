import os, sqlite3
from flask import Flask, g

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'truckz.db'),
    SECRET_KEY = 'truckz.io',
    USERNAME='root',
    PASSWORD='123'
))

def connect_database():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_database():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_database()
    return g.sqlite_db

def init_database():
    db = get_database()
    with app.open_resource('schemas.sql', mode='r') as dbFile:
        db.cursor().executescript(dbFile.read())
    db.commit()

@app.teardown_appcontext
def close_database(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

from truckz.views import auth
from truckz.views import trucks
from truckz.views import owners
from truckz.views import bookings
from truckz.views import journeys
from truckz.views import customers
from truckz.views import dashboard

app.register_blueprint(auth.mod)
app.register_blueprint(trucks.mod)
app.register_blueprint(owners.mod)
app.register_blueprint(bookings.mod)
app.register_blueprint(journeys.mod)
app.register_blueprint(customers.mod)
app.register_blueprint(dashboard.mod)
