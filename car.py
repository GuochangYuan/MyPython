class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=45

	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()

	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer")

	def increment_odometer(self,miles):
		if miles>=0:
			self.odometer_reading+=miles
		else:
			print('增加里程不能为负数')

	def read_odometer(self):
		print('This car has '+str(self.odometer_reading)+" miles on it")

	def fill_gas_tank(self):
		print("汽车油箱")


class Battery():
	
	def __init__(self,battery_size):
		self.battery_size=battery_size

	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-KWh battery.")

	def get_range(self):
		if self.battery_size==70:
			range=240

		elif self.battery_size==85:
			range=270

		message="This car can go approximately "+str(range)
		message+="miles on a full charge"
		print(message)


class ElectricCar(Car):
	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)
		#self.battery_size=70
		self.battery=Battery(70)

	#def describe_battery(self):
		#print("This car has a "+str(self.battery_size)+"-KWh battery.")

	def fill_gas_tank(self):
		print('电动车没有油箱')
