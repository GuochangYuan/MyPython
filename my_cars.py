from car import Car,ElectricCar

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(43)
my_new_car.read_odometer()


my_tesla=ElectricCar('tesla','models',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
