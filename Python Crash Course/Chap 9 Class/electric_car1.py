# definning attributes and methods for the child class
# once a child class has inherited from parent class, you can add any new attributes and methods
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car does need a gas tank.")

class ElectricalCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialized attributes of the parent class
           Then initialize attributes specific to and electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 75                  # newly added attribute
    
    def describe_battery(self):
        """print a statement describe the battery size """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """This method will override parent's fill_gas_tank() function"""
        print("This is electric car which doesn't need gas tank!")

my_tesla = ElectricalCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()