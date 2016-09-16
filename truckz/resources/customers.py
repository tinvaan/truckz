from flask_restful import reqparse, Resource

customer_details = {
    'id': '',
    'name': '',
    'email': '',
    'contact': '',
    'address': '',
    'bookings': {},
    'journeys': {}
}

customers_list = {}

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('contact')
parser.add_argument('address')
parser.add_argument('bookings')
parser.add_argument('journeys')

class Customer(Resource):
    def get(self, cust_id):
        for cust in customers_list:
            if cust.get_id() == cust_id:
                return cust

    def put(self):
        args = parser.parse_args()
        customer = {
            'id': args['id'],
            'name': args['name'],
            'email': args['email'],
            'contact': args['contact'],
            'address': args['address'],
            'bookings': args['bookings'],
            'journeys': args['journeys']
        }
        customers_list.append(customer)

    def get_id():
        return customer_details['id']

    def get_name():
        return customer_details['name']

    def get_email():
        return customer_details['email']

    def get_contact():
        return customer_details['contact']

    def get_address():
        return customer_details['address']

    def get_bookings():
        return customer_details['bookings']

    def get_journeys():
        return customer_details['journeys']

    def set_id(cust_id):
        customer_details['id'] = cust_id

    def set_name(cust_name):
        customer_details['name'] = cust_name

    def set_email(cust_email):
        customer_details['email'] = cust_email

    def set_contact(cust_contact):
        customer_details['contact'] = cust_contact

    def set_address(cust_address):
        customer_details['address'] = cust_address

    def set_bookings(cust_bookings):
        customer_details['bookings'] = cust_bookings

    def set_journeys(cust_journeys):
        customer_details['journeys'] = cust_journeys

class CustomersList(Resource):
    def get(self):
        return

    def put(self):
        return

    def get_customers_list():
        return

    def add(Customer):
        return

    def remove(Customer):
        return
