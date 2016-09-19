import os, sqlite3
from flask import g
from truckz import app

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

@app.teardown_appcontext
def close_database(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_database():
    db = get_database()
    with app.open_resource('schemas.sql', mode='r') as dbFile:
        db.cursor().executescript(dbFile.read())
    db.commit()
