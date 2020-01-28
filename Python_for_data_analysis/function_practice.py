"""FUNCTIONS ARE OBJECTS"""

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

def clean_strings(strings, ops):    # clean_strings is now more reusable    
    result = []                     # generic
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

print(clean_strings(states, clean_ops))

# we can use function as arguments to other functions like the built-in
# map function, which applies a function to a sequence of some kind.
for x in map(remove_punctuation, states):
    print(x)

"""
Anonymous (Lambda) Functions is a way of writing fuction consisting of
single statement, the result of which is the return value. They are
defined by Lambda keyword, which has no meaning other than "we are
declaring an anonymous function.
"""
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

def short_function(x):
    return y * 2

equiv_anon = lambda y: y * 2
print(equiv_anon(2))

""" assign the lambda function to a local variable """
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4,0,1,5,6]
print(apply_to_list(ints, lambda x: x * 2))

# example to sort a collection of strings by the number of distinct letters
# list() function creates a list object
# set() function creates a set object
# sort() method sorts the list ascending by default.
# list.sort(reverse=True|False, key=myFunc). Key=A function to specify the
# sorting criteria(s)

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
list_strings = list(strings)
print(strings)
print(list_strings)
print(list(strings))
print(set(list(strings)))
print(len(set(list(strings))))
strings.sort(key=lambda x: len(set(list(x))))
print(strings)

data = [(4,5,6), (1,2,3), (7,8,9)]
data.sort(key=lambda tup: tup[1])
print(data) 

""" 
Currying: Partial Argument Application. means deriving new functions from
existing ones by partial argument application.
"""
def add_number(x, y):
    return x + y
# using this functioin we could derive a new funciton of one variable, add_five
# that adds  to its argument:
add_five = lambda y: add_number(5, y)
print(add_five(5))
# There is nothing very fancy here. just define a new function to call an
# existing function. The built-in functools module can simplify this process

from functools import partial
add_five = partial(add_number, 10)
print(add_five(5))

""" Generators : iterate over a sequences, like objects in a list or lines in
a file. """
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)
# when you write for key in some_dict, python interpreter first create an
# iterator out of some_dict
dict_iterator = iter(some_dict)
print(dict_iterator)
# an iterator is any object that will yeild objects to the python interpreter
# when used in a context like a for loop. Most methods expecting a list or
# list-like object will also accept any iterable object. e.g. min, max, sun,
# and type constructors like list and tuple
print(list(dict_iterator))

# create generator on request using yield.
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
gen = squares()             # When call the generator, no code is immediately
print(gen)                  # executed.
for x in gen:               # Until you request elements from the generator.
    print(x, end=' ')
    
""" Generator Expressions, to create one, enclose with () instead of [] """
gen = (x ** 2 for x in range(100))
print(gen)
# above code is completely equivalent to following generator verbose累贅的
# generator.
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

""" Generator expression can be used as function argument, instead of list
comprehensions """
gen = (x ** 2 for x in range(100))
print(sum(gen))

print(dict((i, i ** 2) for i in range(5)))

""" itertools module consists of a collection of generators. Usually, it takes
a sequence of data and a function"""
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))     # names is a generator













    












































    
    