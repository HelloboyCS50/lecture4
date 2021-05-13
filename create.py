import os
from flask import Flask , render_template ,request
from models import *


app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/lecture4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
	# flights = db.execute('SELECT * FROM flights').fetchall()

	# USE orm

	flights = Flight.query.all()

	return render_template('index.html' , flights = flights)


@app.route('/book', methods=['POST'])
def book():

	'''Book Flights'''


	name = request.form.get('name')
	try:
		flight_id = int(request.form.get('flight_id'))

	except ValueError:
		return render_template('error.html', message = 'Invaid Flight Number !')

		# If the person give valid flight number...

	# if db.execute('SELECT * FROM flights WHERE id = id' , {'id' : flight_id}).rowcount == 0:

	# Use orm

	flight = Flight.query.get(flight_id)


		return render_template('error.html' , message = 'There are No Flight !')

	# Add passengers

	else:

		# db.execute('INSERT INTO passengers (name , flight_id) VALUES (:name , :flight_id)',
		# 	{"name" : name , "flight_id" : flight_id})

		# Use ORM

		passenger = Passenger(name = name , flight_id = flight_id)



	# db.commit()

	# use ORM

		db.session.add(passenger)
		db.session.commit()
		return render_template('success.html')


@app.route('/flights')

def flights():

	'''List All flights'''

	# flights = db.execute('SELECT * FROM flights').fetchall()

	# Use ORM

	flights = Flight.query.all()


	return render_template('flights.html', flights = flights)


@app.route('/flights/<int:flight_id>')
	
	#List all details about single flight
def flight(flight_id):

	# flight = db.execute('SELECT * FROM flights WHERE id = :id ' , {'id' : flight_id}).fetchone()

	# Use orm

	flight = Flight.query.get(flight_id)

	if flight is None:

		return render_template('error.html' , message = 'No such Flight here..!')

	# Get all passengers

	else:

		passengers = db.execute('SELECT name FROM passengers WHERE flight_id = :flight_id' , {'flight_id' : flight_id}).fetchall()

		# Use ORM

		passenger = Passenger.filter_by(flight_id = flight_id).all()

		return render_template('flight.html' , flight = flight , passengers = passengers )
	