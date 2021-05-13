class Flight:

	def __init__ (self , origin , destination , duration):

		self.origin = origin
		self.destination = destination
		self.duration = duration



def main():

	f = Flight(origin = 'New York' , destination = 'London' , duration = 540)

	# Change or update the value

	f.duration += 10

	print(f.origin)
	print(f.destination)
	print(f.duration)



#This code run main file

if __name__ == '__main__':
	main()