from flask import Flask, Blueprint
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

api_bp = Blueprint('api', __name__)
api = Api(app)

app.register_blueprint(api_bp)

#api.add_resource(Truck, '/trucks/<int: id>')
#api.add_resource(TrucksList, '/trucks')

#api.add_resource(Customer, '/customers/<int: id>')
#api.add_resource(CustomersList, '/customers')

#api.add_resource(Owner, '/owners/<int: id>')
#api.add_resource(OwnersList, '/owners')

#api.add_resource(Booking, '/bookings/<int: id>')
#api.add_resource(BookingsList, '/bookings')

#api.add_resource(Journey, '/journeys/<int: id>')
#api.add_resource(JourneysList, '/journeys')

import truckz.views
