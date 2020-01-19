"""list in Dictionary."""
# Store information about a pizza being ordered.
pizza = { 'crust': 'thick',
          'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 6-7 make 3 dictionaries and store in a list (Dictionary in List)
people_01 = {'first_name': 'mary',
    'last_name': 'Linch',
    'age':30,
    'city': 'Hong Kong'
}
people_02 = {'first_name': 'john',
    'last_name': 'conar',
    'age':29,
    'city': 'USA'
}
people_03 = {'first_name': 'william',
    'last_name': 'Hitch',
    'age':35,
    'city': 'france'
}
peoples = [people_01, people_02, people_03]
for people in peoples:
    for key, value in people.items():
        print(f"{key}: {value}")