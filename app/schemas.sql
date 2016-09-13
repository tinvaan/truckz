pragma foreign_keys = on;

drop table if exists trucks;
create table trucks {
    truck_id integer primary key autoincrement,
    truck_model text not null,
    truck_weight integer not null,
    truck_volume integer not null,
    truck_current_location text,
    truck_registration_number text not null
};

drop table if exists owners;
create table owners {
    owner_id integer primary key autoincrement,
    owner_name text not null,
    owner_email text not null,
    owner_contact integer not null,
    owner_address text,
    foreign key(owner_truck) references trucks(truck_id)
};

drop table if exists customers;
create table customers {
    customer_id integer primary key autoincrement,
    customer_name text not null,
    customer_email text not null,
    customer_contact integer not null,
    customer_address text
};

drop table if exists bookings;
create table bookings {
    booking_id integer primary key autoincrement,
    foreign key(booking_owner_id) references customers(customer_id),
    booking_source_stop text not null,
    booking_destination_stop text not null,
    booking_requested_pickup_date date,
    booking_requested_dropoff_date date,
    foreign key(booking_shipment) references shipments(shipment_id)
};

drop table if exists shipment;
create table shipment {
    shipment_id integer primary key autoincrement,
    foreign key(shipment_booking_id) references bookings(booking_id),
    foreign key(shipment_owner_id) references customers(customer_id),
    shipment_load integer not null,
    shipment_items text,
    shipment_dimensions text not null,
    shipment_approx_wieght integer not null
};

drop table if exists journey_plan;
create table journey_plan {
    journey_id integer primary key autoincrement,
    foreign key(journey_customer_id) references customer(customer_id),
    journey_rate integer not null,
    journey_pickup_date date not null,
    journey_dropoff_date date not null,
};