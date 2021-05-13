# class Flight:

# 	counter = 1

# 	def __init__ (self , origin , destination , duration):

# 		# keep track of id number

# 		self.id = Flight.counter
# 		Flight.counter += 1

# 		# keep track of passengers

# 		self.passengers = []


# 		# Details about flight

# 		self.origin = origin
# 		self.destination = destination
# 		self.duration = duration

# 	def print_info(self):

# 		print(f'Flight origin : {self.origin}')
# 		print(f'Flight destination : {self.destination}')
# 		print(f'Flight duration : {self.duration}')

# 		print()
# 		print('Passengers')
# 		for passenger in self.passengers: # This self.passengers is refar line 14
# 			print(f'{passenger.name}')


# 	def delay(self , amount):
# 		self.duration += amount


# 	def add_passenger(self , p):
# 		self.passengers.append(p) # This self.passengers is refar line 14
# 		p.flight_id = self.id



# class Passenger:

# 	def __init__ (self , name):
# 		self.name = name

# def main():

# 	f1 = Flight(origin = 'London' , destination = 'Dhaka' , duration = 540)

	
# 	alice = Passenger('Alice')

# 	bob = Passenger('Bob')


# 	# Now add

# 	f1.add_passenger(alice)

# 	f1.add_passenger(bob)


# 	f1.print_info()





class Flight:

	counter = 1

	def __init__ (self , origin , destination , duration):

		#keep track id number

		self.id = Flight.counter
		Flight.counter += 1 # Every flight its value encrement  +1

		#keep track passenger

		self.passengers = []






		self.origin = origin
		self.destination = destination
		self.duration = duration

	def flight_info(self):

		print(self.origin)
		print(self.destination)
		print(self.duration)

		print()
		print('passengers :')
		for passenger in self.passengers:
			print(f'{passenger.name}')

	def delay(self , value):
		self.duration += value


	def add_passengers(self , passengername):
		self.passengers.append(passengername)
		passengername.flight_id = self.id



class Passenger:

	def __init__ (self , name):
		self.name = name

def main():

	f1 = Flight('Dhaka' , 'Dubai' , 120)

	alice = Passenger('alice')
	bob = Passenger('bob')
	sara = Passenger('Sara')


	f1.add_passengers(alice)
	f1.add_passengers(bob)
	f1.add_passengers(sara)

	f1.flight_info()















#This code run main file

if __name__ == '__main__':
	main()

