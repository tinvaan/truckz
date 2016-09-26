import operator
from flask import session

from truckz import get_database
from .owners import get_owner_id
from .customers import get_customer_id
from .trucks import get_truck_volume, get_trucks_owned
from .shipments import get_shipment_volume, get_shipment_weight

volumes = {}
trucks_volumes = {}

def get_truck_from_volume():
    return 'work in progress'

def get_truck_id_from_volume():
    return 'work in progress'

'''
Returns the id of the shipment for a booking
'''
def shipment_id_for_booking(booking_id):
    db = get_database()
    cur = db.execute('select booking_shipment from bookings where booking_id = ?', [booking_id])
    row = cur.fetchone()
    return row['booking_shipment']

'''
Fill up the trucks owned with their corresponding
volumes and sort the list
'''
def populate_trucks_with_volumes():
    for truck in get_trucks_owned():
        trucks_volumes[truck['truck_id']] = get_truck_volume(truck['truck_id'])

    trucks_volumes = sorted(trucks_volumes.items(), key=operator.itemgetter(1))
    extract_truck_volumes()

'''
Get only the volumes from the dict containing
truck volumes and truck id's.
@ret Returns a list.
'''
def extract_truck_volumes():
    for i in range(0, len(trucks_volumes)):
        volumes.append(trucks_volumes[i][1])
    volumes = list(volume)

def truck_for_shipment(s_id):
    s_volume = get_shipment_volume(s_id)

    if s_volume < trucks_volumes[0][1]:
        return None
    else:

def closest_matching_truck_volume(v, s_volume):
    if len(v) == 1:
        if v[0] <= s_volume:
            return get_truck_from_volume(v[0])
        else:
            return None

    if s_volume < v[int(len(v)/2)]:
        v = v[0:int(len(v/2))]
        closest_matching_truck_volume(v, s_volume)
    else:
        v = v[int(len(v/2)):len(v)]
        closest_matching_truck_volume(v, s_volume)

def partial_journey_wrapper(s_volume):
    volumes = sorted(volumes)
    closest_volume = closest_match(volumes, summation)
    index = volumes.index(closest_volumes)
    return partial_journey_trucks(index, summation)

def partial_journey_trucks(index, s_volume, temp=[]):
    if not index is None:
        if index == 0:
            if volumes[index] == summation:
                temp.append(s_volume)
                return temp
            else:
                return None

        rem = s_volume - volumes[index]
        temp.append(volumes[index])
        try:
            if volumes.index(rem):
                temp.append(rem)
                return temp
        except ValueError:
            index = index -1
            partial_journey_trucks(index, s_volume, temp)
    else:
        return None
