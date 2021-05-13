from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):

	__tablename__ = 'flights'

	id = db.Column(db.Integer , primary_key=True)
	origin = db.Column(db.String , nullable=False)
	destination = db.Column(db.String , nullable=False)
	duration = db.Column(db.Integer , nullable=False)
	passengers = db.relationship("Passenger" , backref = "flight", lazy = True)


	# def add_passenger(self , name):

	# 	p = Passenger(name=name , flight_id=self.id)
	# 	db.session.add(p)
	# 	db.session.commit()



# In command line this is like this

	# 	CREATE TABLE flights (

# 	id SERIAL PRIMARY KEY,
# 	origin VARCHAR NOT NULL,
# 	destination VARCHAR NOT NULL,
# 	duration INTEGER NOT NULL

# );

	# def add_passenger(self , name):

	# 	p = Passenger(name=name , flight_id=self.id)
	# 	db.session.add(p)
	# 	db.session.commit()


class Passenger(db.Model):

	__tablename__ = 'passengers'
	id = db.Column(db.Integer , primary_key = True)
	name = db.Column(db.String , nullable = False)
	flight_id = db.Column(db.Integer , db.ForeignKey('flights.id') , nullable = False)



# In command line this is like this


# CREATE TABLE passengers (

# 	id SERIAL PRIMARY KEY,
# 	name VARCHAR NOT NULL ,
# 	flight_id INTEGER REFERENCES flights


# );










