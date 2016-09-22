pragma foreign_keys = on;

drop table if exists trucks;
create table trucks (
    truck_id integer primary key autoincrement,
    truck_model text not null,
    truck_weight integer not null,
    truck_volume integer not null,
    truck_current_location text,
    truck_registration_number text not null
);
/* Insert dummy trucks data */
insert into trucks values(1, "Tata Ace", 1500, 1500, "Pallavaram", "TN 01 AB007");
insert into trucks values(2, "Ashok Leyland", 3000, 3000, "Mambalam", "TN 01 BE619");

drop table if exists owners;
create table owners (
    owner_id integer primary key /*autoincrement*/,
    owner_auth_username text not null,
    owner_auth_password text not null,
    owner_name text,
    owner_email text,
    owner_contact integer,
    owner_address text,
    owner_trucks integer/*,
    foreign key(owner_trucks) references trucks(truck_id)*/
);
/* Insert dummy owner data */
insert into owners values(1, "harish", "navnit", "Harish", "harish@mail.com", 9246262623, "", 1);
insert into owners values(2, "laurent", "koscielny", "Kos", "kos@afc.com", 3125513535, "", 2);

drop table if exists customers;
create table customers (
    customer_id integer primary key /*autoincrement*/,
    customer_auth_username text not null,
    customer_auth_password text not null,
    customer_name text,
    customer_email text,
    customer_contact integer,
    customer_address text
);
/* Insert dummy customer data */
insert into customers values(1, "harish", "navnit", "Harish", "harish@mail.com", 9246262623, "");
insert into customers values(2, "mesut", "ozil", "MO", "ozil@afc.com", 1126163626, "");


drop table if exists bookings;
create table bookings (
    booking_id integer primary key /*autoincrement*/,
    booking_owner_id integer,
    booking_source_stop text not null,
    booking_destination_stop text not null,
    booking_requested_pickup_date date,
    booking_requested_dropoff_date date,
    booking_shipment integer/*,
    foreign key(booking_owner_id) references customers(customer_id),
    foreign key(booking_shipment) references shipments(shipment_id)*/
);

drop table if exists shipments;
create table shipments (
    shipment_id integer primary key /*autoincrement*/,
    shipment_booking_id integer,
    shipment_owner_id integer,
    shipment_load integer not null,
    shipment_items text,
    shipment_dimensions text not null,
    shipment_approx_wieght integer not null/*,
    foreign key(shipment_booking_id) references bookings(booking_id),
    foreign key(shipment_owner_id) references customers(customer_id)*/
);

drop table if exists journey_plan;
create table journey_plan (
    journey_id integer primary key autoincrement,
    journey_customer_id integer,
    journey_rate integer not null,
    journey_pickup_date date not null,
    journey_dropoff_date date not null/*,
    foreign key(journey_customer_id) references customers(customer_id)*/
);
