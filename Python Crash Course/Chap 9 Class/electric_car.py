"""A class that can be used to represent a car."""
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


class Battery:
    """This class serves : Instances as attributes. In the process of writing code,
       more and more details are adding to a class. A growing list of methods and attributes
       make the file becoming lengthy. some parts can be written as a separate class.
       class battery is used as attributes and methods for ElectricalCar.
    """
    def __init__(self, battery_size=75):
        self.battery_size = battery_size  # instance as attribute

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full charge.")

class ElectricalCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """initialized attributes of the parent class
           Then initialize attributes specific to and electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # newly added attribute

    def fill_gas_tank(self):
        """This method will override parent's fill_gas_tank() function"""
        print("This is electric car which doesn't need gas tank!")


my_tesla = ElectricalCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
