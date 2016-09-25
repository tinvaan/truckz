from flask import Blueprint
from truckz import get_database
 
def get_shipments_weight(s_id):
    db = get_database()
    cur = db.execute('select shipment_approx_weight from shipments where shipment_id = ?', [s_id])
    row = cur.fetchone()
    return row['shipment_approx_weight']

def get_shipments_volume(s_id):
    db = get_database()
    cur = db.execute('select shipment_dimensions from shipments where shipment_id = ?', [s_id])
    row = cur.fetchone()

    dimensions = row['shipment_dimensions']
    separator = dimensions.index('x')
    width = dimensions[0:separator]
    height = dimensions[separator+1:len(dimensions)]
    return int(height) * int(width)
