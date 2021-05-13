class Flight:

	def __init__ (self , origin , destination , duration):

		self.origin = origin
		self.destination = destination
		self.duration = duration

	def flight_info(self):

		print(f'Flight origin : {self.origin}')
		print(f'Flight destination : {self.destination}')
		print(f'Flight duration : {self.duration}')



def main():

	f1 = Flight(origin = 'London' , destination = 'Dhaka' , duration = 540)

	# Another way to do this

	# f1 = Flight('London' ,'Dhaka' ,540)

	f1.flight_info()


	# f2 = Flight(origin = 'Canada' , destination = 'Hawaie' , duration = 420)

	# Another way to do this

	f2 = Flight('Canada' , 'Hawaie' , 420)

	f2.flight_info()



#This code run main file

if __name__ == '__main__':
	main()