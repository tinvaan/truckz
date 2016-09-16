from flask_restful import  reqparse, Resource

truck_details = {
    'id': '',
    'model': '',
    'weight': '',
    'volume': '',
    'curr_location': '',
    'reg_number': ''
}

trucks_list = {}

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('model')
parser.add_argument('weight')
parser.add_argument('volume')
parser.add_argument('curr_location')
parser.add_argument('reg_number')

class Truck(Resource):

    def get(self, truck_id):
        for truck in trucks_list:
            if truck.get_id() == truck_id:
                return truck

    def put(self):
        args = parser.parse_args()
        truck = {
            'id': args['id'],
            'model': args['model'],
            'weight': args['weight'],
            'volume': args['volume'],
            'curr_location': args['curr_location'],
            'reg_number': args['reg_number']
        }
        trucks_list.append(truck)

    def get_id(self):
        return truck_details['id']

    def get_model(self):
        return truck_details['model']

    def get_weight(self):
        return truck_details['weight']

    def get_volume(self):
        return truck_details['volume']

    def get_current_location(self):
        return truck_details['curr_location']

    def get_registration_number(self):
        return truck_details['reg_number']

    def set_id(self, truck_id):
        truck_details['id'] = truck_id

    def set_model(self, model):
        truck_details['model'] = model

    def set_weight(self, weight):
        truck_details['weight'] = weight

    def set_volume(self, volume):
        truck_details['volume'] = volume

    def set_current_location(self, location):
        truck_details['curr_location'] = location

    def set_registration_number(self, number):
        truck_details['reg_number'] = number

class TrucksList(Resource):
    def get(self):
        return

    def put(self):
        return

    def get_trucks_list(self):
        return trucks_list

    def add(Truck):
        trucks_list.append(Truck)

    def remove(Truck):
        return
