"""
Contains the general setup/config of the application.
"""

import os
from flask import Flask, Blueprint
from flask_restful import Api

from app.trucks import Trucks
from app.owners import Owners
from app.customers import Customers

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

app.register_blueprint(api_bp)
