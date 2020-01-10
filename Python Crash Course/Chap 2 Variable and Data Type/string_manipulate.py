# escape character \ lets you use characters that are otherwise impossible to put into a string.
spam = 'Say hi to Bob\'s mother.'
print(spam)

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings r completely ignores all escape characters and prints any backslash that appears in the string
print(r'That is Carol\'s cat.')
print(r'C:\Users\Al\Desktop')

# Triple Quotes : Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.
print('''Dear Alice,

    Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Indexing and Slicing Strings
spam = 'Hello, world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[:5])

# The in and not in Operators with Strings
print('Hello' in 'Hello, World')
print('HELLO' in 'Hello, World')
print('cats' not in 'cats and dogs')

# Putting Strings Inside Other Strings
name = 'Al'
age = 4000
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')

# %s operator inside the string acts as a marker to be replaced by values following the string
name = 'John'
age = 300
print('My name is %s. I am %s years old.' %(name,age))

# Python 3.6 introduced f-strings
print(f"My name is {name}. I am {age} years old.")

# isupper(), and islower() Methods
spam = 'Hello, world!'
print(spam.islower())

print('HELLO'.isupper())
print('HELLO'.lower().islower())

"""
isalpha() Returns True if the string consists only of letters and isn’t blank
isalnum() Returns True if the string consists only of letters and numbers and is not blank
isdecimal() Returns True if the string consists only of numeric characters and is not blank
isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
"""

# The startswith() and endswith() Methods
print('Hello, world!'.startswith('Hello'))
print('abc123'.endswith('12'))

# The join() and split() Methods
print('.'.join(['cats', 'rats', 'bats']))
print('-'.join(['cats', 'rats', 'bats']))
print('  '.join(['cats', 'rats', 'bats']))
print('My name is Simon'.split())
print('MyABC nameABC isABC Simon'.split('ABC'))
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

# partition() can split a string into the text before and after a separator string.
# This method searches the string it is called on for the separator string it is passed,
# and returns a tuple of three substrings for the “before,” “separator,” and “after” substrings.
print('Hello, world!'.partition('w'))

# rjust(), ljust(), and center()
print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.ljust(10,'*'))
print('Hello'.center(20, '='))

# strip(), rstrip(), and lstrip()
print('    Hello, World    '.strip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

# Numeric Values of Characters with the ord() and chr() Functions https://youtu.be/sgHbC6udIqc.
print(ord('A'))
print(chr(65))
print(ord('A') < ord('B'))
print(chr(ord('A')))
print(chr(ord('A') + 1))

# Copying and Pasting Strings with the pyperclip Module
import pyperclip
pyperclip.copy('Hello, World')
pyperclip.paste()





