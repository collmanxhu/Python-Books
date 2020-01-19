# loop through a dictionary, polling gram to store poll response
responses = {}
polling_active = True     # set flag to indicate poll is active
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain you like most? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    for name, response in responses.items():    # polling is complete, show results
        print(f"\n{name} likes {response} the most.")

# 7-8 make a list and fill it with names of various sandwiches
unfinished_sandwiches = ['Bacon', 'Beef', 'Cheese', 'Chicken', 'Tuna']
finsihed_sandwiches = []
while unfinished_sandwiches:
    made_sandwiches = unfinished_sandwiches.pop()
    print(f"\nI made your {made_sandwiches.title()} sandwiches.")
    finsihed_sandwiches.append(made_sandwiches)
print("\nThe following sandwiches are made: ")
for finished_sandwich in finsihed_sandwiches:
    print(f"{finished_sandwich.title()} sandwiches")

# 7-9 no Pastrami in the list
unfinished_sandwiches = ['Bacon','Pastrami','Beef','Pastrami''Cheese','Chicken','Pastrami','Tuna']
print("\nWe are sorry that Pastrami has run out of stock.")
while 'Pastrami' in unfinished_sandwiches:
    unfinished_sandwiches.remove('Pastrami')
print(unfinished_sandwiches)

# 7-10 Polls users about their dream vacation
vacations = {}
polling_active = True
while polling_active:
    name = input("\nWhats your name?")
    vacation = input("\nPlease provide the place you want vacation. ")
    vacations[name] = vacation
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
for name, vacation in vacations.items():
    print(f"\n{name.title()} would like to take vacation at {vacation.title()}.")
