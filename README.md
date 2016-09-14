Design and build the API for a truck booking platform - Truckz.io

###Requirements:

1. The Truckz.io platform should be able to categorize and list several models of trucks with their max weight and
   volume info. ( Tata Ace Mini - 1 Tonne, holds 450 cubic meters )

2. Truck owners should be able to list truck vehicles from the above models. ( ie, he should be able to add 2 Tata Ace Mini,
   3 Ashok Leyland 2516L trucks etc ). He should also be able to override the capacity information if he has customized the truck.
   Each truck should be uniquely identifiable by number plate.

3. A customer (one who wants to transport some goods) should be able to place a booking request - mentioning the source and destination. He should specify the items to be transported, their total approx weight and their dimensions (to calculate the volume). He should also mention the desired pickup date and time and the desired drop off date and time

4. Truck owners should be able to view these booking requests placed by customers. They should be able to respond to these
   requests with proposed journey plans. A journey plan could be offered either as
   
   a. A full truck end to end booking - with the entire truck ( of any appropriate size based on customer's request ) booked solely for that customer with pickup and drop off at customer's mentioned addresses. Truck owner should be able to provide the full rate for the journey and the proposed pickup and dropoff date and time ( which may or may not match with what the customer mentioned as desirable in his request)

   b. Provide partial space in a bigger truck, where this customer's goods will be transported along with the goods of other customers. This can further be of 2 types
      
      i. End to end - the truck will pick up at customer's source and stop at the customer's desired destination and drop off the goods and then proceed to deliver other goods to other customers
     
     ii. Either the pickup or drop off or both - will be at some other nearby spot where the customer has to either go and
         drop off the goods (in case of pickup) or pickup the goods (in case of dropoff spot) at a specified date and time.
         In both i and ii - the truck owner should mention the rates and pickup and dropoff dates

  A customer will be able to view his booking request and the different journey plans and compare them and book one.
  
  Also, the truck owners should be able to see where any given truck's last destination stop was. (Not required to be tracked realtime. But since the platform knows the last journey it made and where the final destination was, it can mark that city as the truck's current city.)
  
###Problem Statement:

Design and implement the schema and a REST API for a truck booking platform with the above requirements. 

While having a HTML/JS frontend for the platform would be nice - it is not mandatory - you can do it optionally if you have time.
And regarding the requirements - upto section 4a, they are quite straightforward to implement. Section 4b is likely to
be comparitively harder. It is meant as an advanced section which can be attempted after completing the previous requirements.

The requirements while being defined to some extent, still leave a lot to your creativity. Please feel free to assume any
other constraints that you think should apply while designing the schema and API. You can also add more features which are not mentioned in the requirements for bonus points. 

###What tools to use?

We use a python stack on the backend with Flask as the web framework and SQLAlchemy as the ORM at Inkmonk. So if you
are familiar with it and use it to solve this problem - it would be great. But it is not a requirement. You can use Django or Rails or any framework that you are comfortable with.

  
