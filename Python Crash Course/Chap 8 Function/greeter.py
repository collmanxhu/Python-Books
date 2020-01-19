def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()          #call the function to perform

def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')

# 8-1 use function to display message
def display_message():
    print("Hi all, I am learning python in chapter 8.")
display_message()

# 8-2 use function to take argument and display message
def favorite_book(book):
    print(f"One of my favorite books is {book.title()}.")
favorite_book('Game of Throne')

# positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

# keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='dog', pet_name='Xijinping')

# default values of argument
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='Xijinping')
describe_pet('harry', 'hamster')
describe_pet(animal_type='horse', pet_name='dada')

# function to return value
def get_formatted_name(first_name, last_name):
    """Return a ull name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# function with optional value
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('john', 'lee')
print(musician)


# function to return dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information of a person """
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('michael', 'jackson')
print(musician)


# function to return dictionary with optional argument
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information of a person """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('michael', 'jackson', 27)
print(musician)

# using function with while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 8-6 use function to return city and country
def get_city_name(city, country):
    full_city_name = f"{city}, {country}"
    return full_city_name
city = get_city_name('hong kong', 'china')
print(city)
city = get_city_name('osaka', 'japan')
print(city)
city = get_city_name('london', 'Britain')
print(city)

# 8-7 use function to make dictionary of album information
def make_album(artist, album, year=None, genre=''):
    """Return a dictionary of music album"""
    full_album = {'artist': artist, 'album': album}
    if year:
        full_album['year'] = year
    if genre != '':
        full_album['genre'] = genre
    return full_album
while True:
    print("\nPlease input album details.")
    print("(You can quit by typing 'q' at any time.")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    year = input("Year: ")
    if year == 'q':
        break
    if year.isdigit():
        year = int(year)
    genre = input("Genre: ")
    if genre == 'q':
        break
    music_alblum = make_album(artist, album, year, genre)
    print(music_alblum)

# passing a list to function
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['peter', 'hannah', 'ty', 'margot']
greet_users(usernames)

# modifying list in a function
# first try without using function
unprinted_designs = ['phone', 'case', 'robot pendant', 'dodecahedron']
completed_models = []
# stimulate printing each design, move each design to completed models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    completed_models.append(current_design)
    print(f"Printing models : {current_design}")
    # display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# rewrite above code using functions: handle printing, summarize the prints
def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
        print(f"Printing model: {current_design}")

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone', 'case', 'robot pendant', 'dodecahedron']
completed_models = []
print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)