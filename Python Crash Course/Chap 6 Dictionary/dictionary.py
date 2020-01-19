favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
language = favorite_languages['jen'].title()
print(f"Jen's favorite languages is {language}.")

"""The get() method requires a key as a first argument. As a second optional
 argument, you can pass the value to be returned if the key doesn’t exist:"""
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('point', 'No point value')
#point_value = alien_0.get('point')
print(point_value)

#6-1 use dictionary to store a person information
mary = {'first_name': 'mary',
    'last_name': 'Linch',
    'age':30,
    'city': 'Hong Kong'
    }
print(f"Mary's first name is {mary['first_name'].title()} and" \
    f" last name is {mary['last_name']}. She is age {mary['age']} and" \
    f" lives in {mary['city']}.")
    
#6-2 use dictionary to store luck number of 5 person
lucky_number = {
    'peter': 35, 
    'adam': 79,
    'cecilius': 64,
    'angela':13,
    'john': 89
    }
print(f"The lucky number of Peter is {lucky_number['peter']}.")
print(f"The lucky number of Adam is {lucky_number['adam']}.")
print(f"The lucky number of Cecilius is {lucky_number['cecilius']}.")
print(f"The lucky number of Angela is {lucky_number['angela']}.")
print(f"The lucky number of John is {lucky_number['john']}.")

#6-3 Glossary
program_words = {
    'key': 'Key is connected to a value in dictionary',
    'value': 'Value is data representing a specific key',
    'get()': 'get() function is used to retreive value of a key',
    'sorted()': 'sorted() function is used to sorted a list/dictionary in order',
    'for loop': 'for loop is used to loop over a collection of object/list/dictionary'
    }
print(f"Key: {program_words['key']}.")
print(f"Value: {program_words['value']}.")
print(f"get(): {program_words['get()']}.")
print(f"sorted(): {program_words['sorted()']}.")
print(f"for loop: {program_words['for loop']}.")

user_0 = {
    'username': 'joejoe',
    'first': 'harrison',
    'last': 'joe'
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages is {language}.")

"""The keys() method is useful when you don’t need
 to work with all of the values in a dictionary."""
for name in favorite_languages.keys():
    print(name.title())
    
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for polling.")

for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):    #use set() to avoid repetitive values
    print(language.title())

languages = {'python', 'c', 'ruby', 'c++'}           #build set using {}, sets do not retain items in any specific order.
print(languages)

#6-4 Glossary : use for loop
program_words = {
    'key': 'Key is connected to a value in dictionary',
    'value': 'Value is data representing a specific key',
    'get()': 'get() function is used to retreive value of a key',
    'sorted()': 'sorted() function is used to sorted a list/dictionary in order',
    'for loop': 'for loop is used to loop over a collection of object/list/dictionary'
    }
for program_word, program_meaning in program_words.items():
    print(f"{program_word.title()} : {program_meaning.title()}.")

rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'yangtze': 'china'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# List of dictionaries
alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# create a fleet of 30 aliens
aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(f"\nThe total number of aliens is {len(aliens)}.")

# change first three aliens to yellow, medium-speed, 10 points
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)

# setdefault() set a value in a dictionary for a certain key
# nly if that key does not already have a value
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)




















    
