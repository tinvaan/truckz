import sqlite3
from flask import g
from app import app

class app_db:
    def __init__(self):
        connection = self.connect_db()
        db = self.get_database()

    def connect_db():
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn

    def get_database(self):
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = self.connect_db()
        return g.sqlite_db

    @app.teardown_appcontext
    def close_database():
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()

    def init_database(self):
        db = self.get_database()
        with app.open_resource('schemas.sql', mode='r') as dbFile:
            db.cursor().executescript(dbFile.read())
        db.commit()
