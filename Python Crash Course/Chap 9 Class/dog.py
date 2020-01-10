class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age, sex):
        self.name = name  # initialize name, age and sex
        self.age = age
        self.sex = sex

    def sit(self):
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6, 'f')
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

# 9-1 make restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print(f"{self.restaurant_name} restaurant is doing {self.cuisine_name}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is opening now.")

rest = Restaurant('La La', 'chinese')
print(f"The restaurant name is {rest.restaurant_name}.")
print(f"The cuisine name is {rest.cuisine_name}.")
print(rest.describe_restaurant())
print(rest.open_restaurant())

# 9-2 create 3 different instances from #9-1 and call describe_restaurant
rest = Restaurant('Tai Pan', 'Thai')
print(rest.describe_restaurant())
rest = Restaurant('Maxim', 'French')
print(rest.describe_restaurant())

# 9-3 create a class to display user info and make method call
class User:
    def __init__(self, first_name, last_name, sex, age, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.birth_date = birth_date

    def describe_user(self):
        print("\nHere are the user info:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"sex: {self.sex}")
        print(f"Age: {self.age}")
        print(f"Birth date: {self.birth_date}")

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, I am happy to meet you.")

tag_user = User('collman', 'chu', 'M', 54, '27/12/1966')
print(tag_user.describe_user())
print(tag_user.greet_user())

# set a default value for an attribute
class Car:
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      # set default value

    def get_descriptive_name(self):
        long_name = (f"{self.year} {self.make.title()} {self.model}")
        return long_name.title()

    def read_odometer(self):
        """print a statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
# modify an attribute's value through method
    def update_odometer(self, mileage):
        """set the odometer reading to the given value"""
        self.odometer_reading = mileage
# increment an attribute's value through method
    def increment_odometer(self, miles):
        """add the give amount to the odometer"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
my_new_car.get_descriptive_name()
my_new_car.read_odometer()

# modify an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modify an attribute's value through method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# increment an attribute's value through method
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# 9-4 Number served : add an attribute value with a default value, add method to set customers number
class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0                   # set default value
        self.flavors = ['chocolate', 'mint', 'straw berry', 'vanilla']   # 9-6 exercise

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_num):
        self.number_served += increment_num

    def get_ice_cream_flavors(self):
        """ 9-6 exercise """
        print("\nThe ice cream stand has following flavors:")
        for flavor in self.flavors:
            print(f"\t-- {flavor}")

restaurant = Restaurant('LA LA', 'Thai')
print(f"Served customers: {restaurant.number_served}")
restaurant.set_number_served(26)
print(f"Served customers: {restaurant.number_served}")
restaurant.increment_number_served(2)
print(f"Number of customers increment: {restaurant.number_served}")

# 9-6 add an attribute called flavors, write a method to display flavors
restaurant.get_ice_cream_flavors()

# 9-7 add an Admin class with attributes and method
class User:
    def __init__(self, first_name, last_name, sex, age, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.birth_date = birth_date

    def describe_user(self):
        print("\nHere are the user info:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"sex: {self.sex}")
        print(f"Age: {self.age}")
        print(f"Birth date: {self.birth_date}")

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, I am happy to meet you.")

class Admin(User):
    def __init__(self, first_name, last_name, sex, age, birth_date):
        super().__init__(first_name, last_name, sex, age, birth_date)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print(f"\nAdmin has following privileges:")
        for privilege in self.privileges:
            print(f"-- {privilege}")

admin = Admin('John', 'Snow', 'M', 36, '15/9/1991')
admin.show_privileges()

# 9-8 add a class Privileges with attribute to store a list
class User:
    def __init__(self, first_name, last_name, sex, age, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.birth_date = birth_date

    def describe_user(self):
        print("\nHere are the user info:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"sex: {self.sex}")
        print(f"Age: {self.age}")
        print(f"Birth date: {self.birth_date}")

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, I am happy to meet you.")

class Privileges:
    def __init__(self):
        self.privileges = ['can add post1', 'can delete post1', 'can ban user1']
    def show_privileges(self):
        print(f"\nAdmin has following privileges:")
        for privilege in self.privileges:
            print(f"-- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, sex, age, birth_date):
        super().__init__(first_name, last_name, sex, age, birth_date)
        self.privileges = Privileges()

admin = Admin('John', 'Snow', 'M', 36, '15/9/1991')
admin.privileges.show_privileges()
