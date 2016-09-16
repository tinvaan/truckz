from flask_restful import reqparse, Resource

owner_details = {
    'id': '',
    'name': '',
    'email': '',
    'contact': '',
    'address': '',
    'trucks': {}
}

owners_list = {}

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('contact')
parser.add_argument('addresss')
parser.add_argument('trucks')

class Owner(Resource):
    def get(self, owner_id):
        for owner in owners_list:
            if owner.get_id() == owner_id:
                return owner

    def post(self):
        args = parser.parse_args()
        owner = {
            'id': args['id'],
            'name': args['name'],
            'email': args['email'],
            'contact': args['contact'],
            'address': args['address'],
            'trucks': args['trucks']
        }
        owners_list.append(owner)

    def get_id():
        return owner_details['id']

    def get_name():
        return owner_details['name']

    def get_email():
        return owner_details['email']

    def get_contact():
        return owner_details['contact']

    def get_address():
        return owner_details['address']

    def get_trucks_owned():
        return owner_details['trucks']

    def set_id(self, owner_id):
        owner_details['id'] = owner_id

    def set_name(self, owner_name):
        owner_details['name'] = owner_name

    def set_email(self, owner_email):
        owner_details['email'] = owner_email

    def set_contact(self, owner_contact):
        owner_details['contact'] = owner_contact

    def set_trucks_owned(self, owner_trucks):
        owner_details['trucks'] = owner_trucks

class OwnersList(Resource):
    def get(self):
        return

    def put(self):
        return

    def get_owners_list(self):
        return owners_list

    def add(Owner):
        return

    def remove(Owner):
        return
