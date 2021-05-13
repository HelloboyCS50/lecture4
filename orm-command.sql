from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


***************************************************************************

class Flight(db.Model):

	__tablename__ = 'flights'

	id = db.Column(db.Integer , primary_key=True)
	origin = db.Column(db.String , nullable=False)
	destination = db.Column(db.String , nullable=False)
	duration = db.Column(db.Integer , nullable=False)

# In command line this is like this

	 	CREATE TABLE flights (

 	id SERIAL PRIMARY KEY,
 	origin VARCHAR NOT NULL,
 	destination VARCHAR NOT NULL,
 	duration INTEGER NOT NULL

 );


*******************************************************************************

class Passenger(db.Model):

	__tablename__ = 'passengers'
	id = db.Column(db.Integer , primary_key = True)
	name = db.Column(db.String , nullable = False)
	flight_id = db.Column(db.Integer , db.ForeignKey('flights.id') , nullable = False)



# In command line this is like this


CREATE TABLE passengers (

 	id SERIAL PRIMARY KEY,
 	name VARCHAR NOT NULL ,
 	flight_id INTEGER REFERENCES flights


);


**********************************************************************************

# Insert data in database


flight = Flight(origin = 'London' , destination = 'London' , destination = 540)

db.session.add(flight)


# In command line like this

INSERT INTO flights(origin , destination , duration) VALUES ('London' , 'London' , 540)


**********************************************************************************

# In ORM

Flight.query.all()



# # In commmand line

SELECT * FROM flight;


***********************************************************************************

# See specific one flight details

SELECT * FROM flight WHERE origin = 'Paris';

# In ORM command line

Flight.query.filter_by(origin ='Paris').all()



***********************************************************************************

# To update in the database

UPDATE flights SET duration = 200 WHERE id = 6;


# IN ORM

flight = Flight.query.get(6)

flight.duration = 280

**********************************************************************************


# TO delete 

DELETE form flights WHERE id = 28 ;

flight = Flight.query.get(28)

db.session.delete(flight)










