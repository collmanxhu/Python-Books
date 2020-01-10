# while loop 
number_count = 1
while number_count <= 5:
    print(number_count)
    number_count += 1

# use conditional test to stop the loop
prompt = "\nTell me something, I'll repeat it back to you."
prompt += "\nEnter 'exit' to end the program. "
message = ""
while message != 'exit':
    message = input(prompt)
    if message != 'exit':
        print(message)

# use flag to terminate a program
prompt = "\nTell me something, I'll repeat it back to you."
prompt += "\nEnter 'exit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'exit':
        active = False
    else:
        print(message)

# using break to exit loop
prompt = "\nTell me the city name you have visited."
prompt += "\nEnter 'exit' when you are finished. "
while True:
    city = input(prompt)
    if city == 'exit':
        break
    else:
        print(f"I'd love to go to {city.title()}.")
        
# using continue in a Loop
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)

# 7-4 pizza toppings
prompt = "\nTell me the toppings you like."
prompt += "\nEnter 'exit' when you are finished. "
while True:
    order = input(prompt)
    if order == 'exit':
        break
    else:
        print(f"Toppings {order.title()} is added.")

# 7-5 use three versions to stop a loop
prompt = "\nTell me the age, I'll tell the ticket price."
prompt += "\nEnter 'exit' when you are done. "
age = ""
while age != 'exit':
    age = input(prompt)
    if age.isdigit():
        age = int(age)
        if age <= 3:
            print(f"\nThe ticket price for {age} is free.")
        elif 3 < age <= 12:
            print(f"\nThe ticket price for {age} is $10.")
        elif age > 12:
            print(f"\nThe ticket price for {age} is $15.")

prompt = "\nTell me the age, I'll tell the ticket price. (3 versions)"
prompt += "\nEnter 'exit' when you are done. "
flag = True
while flag:
    age = input(prompt)
    if age == 'exit':
        flag = False
    elif age.isdigit():
        age = int(age)
        if age <= 3:
            print(f"\nThe ticket price for {age} is free.")
        elif 3 < age <= 12:
            print(f"\nThe ticket price for {age} is $10.")
        elif age > 12:
            print(f"\nThe ticket price for {age} is $15.")

# loop through list