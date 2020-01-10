cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)

    age = 12
    if age < 4:
        print('your admission cost is &0')
    elif age > 4 and age <18:
        print('your admission cost is $25')
    else:
        print('your admission cost is $40')
    
    age = 12
    if age < 4:
        price = 0
    elif age > 4 and age <18:
        price = 25
    else:
        price = 40
    print(f"your admission cost is ${price}.")

