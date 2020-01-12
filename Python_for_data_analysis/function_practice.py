def my_func():
    a = 10
    b = 56
    c = 47
    return a, b, c

x, y, z = my_func()
print(x, y, z)          # the function is actually just returning one object, namely a tuple,

def f():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}

print(f())

"""Function is object, so many constructs can be easily expressed 
"""
# below are inputs from submitted survey data. One way to clear the mess is to use built-in strings
# methods along with 're' standard lib module for regular expressions
states = ['Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']

import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

print(clean_strings(states))

# An alternative approach that you may find useful is to mmake a list of the
# operation you want to apply to a particular set of strings
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

print(clean_strings(states, clean_ops))



        
