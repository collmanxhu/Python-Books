# 	url = git@github.com:/collmanxhu/Python.git
a_list = '2 3 7 None'.split()
print(a_list)

a_list = [2, 3, 7, None]
print(a_list)

tup = 'foo bar baz'.split()
b_list = list(tup)
print(b_list)

b_list[1] = 'peekaboo'
print(b_list)

gen = range(10)
print(list(gen))

seq1 = [ 'foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
seq3 = [False, True]

print(list(zip(seq1, seq2, seq3)))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print(f"{i}: {a}, {b}")

print(list(reversed(range(10))))   # keep in mind that reversed is a generator, so it does not create the reversed sequence until materialized

"""
concatenation by addition is a comparatively expensive operation, since a new
list must be created and the objects copied over. Using 'extend' to append
elements to append.
"""
everything = []
list_of_lists = ['1', '6', 'type', '6', 'help']
for chunk in list_of_lists:
    everything.extend(chunk)

print(everything)

# sort for strings length
b = ['saw', 'small', 'He', 'foxes', 'appearance', 'six', 'happy']
b.sort(key=len)
print(b)

import bisect
c = [1,2,2,2,3,4,7]
print(bisect.bisect(c, 2))
print(c)

# enumerate returns a sequence of (i, value)tuples
# i = 0
# for vaule in collection:
#   do something with value
#   i += 1
# above is very common to keep track of the index of current. use enumerate instead

# for i, value in enumerate(collection):
#   do something with value
some_list = ['foo', 'bar', 'baz', 'apple']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)
by_letter['c'] = 'cat'
print(by_letter)
by_letter['c'] = ['catch']
print(by_letter)
by_letter['c'].append('crowd')
print(by_letter)

# the setdefault dict method is for precisely this purpose.
words = ['hat', 'dat', 'dar', 'hom', 'java', 'julie']
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
print(by_letter)

# A set is an unordered collection of unique elements.
my_set = {2,2,2,1,3,6,8}
print(set(my_set))

a = {1 , 2 , 3 , 4 , 5}
b = {3 , 4 , 5 , 6 , 7 , 8}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)
c = a.copy()
c |= b                  # Set the contents of a to be the union of the elements in a and b
print(c)                # Refer Python for Data Analysis page 102
d = a.copy()
d &= b                  # Set the contents of a to be the intersection of the elements in a and b
print(d)

# List Comprehensions
# [ expr for val in collection if condition ]
strings = ['a' , 'as' , 'bat' , 'car' , 'dove' , 'python']
print([x.upper () for x in strings if len (x) > 2])

# Dict & Set comprehension
# dict_comp = { key-expr : value-expr for value in collection if condition }
# set_comp = { expr for value in collection if condition }

unique_lengths = {len(x) for x in strings}          # create a set
print(unique_lengths)
print(set(map(len, strings)))

loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)

# to get 2 or more 'e' from the list
all_data = [['John' , 'Emily' , 'Michael' , 'Mary' , 'Steven'], ['Maria' , 'Juan' , 'Javier' , 'Natalia' , 'Pilar']]
name_of_interest = []
for names in all_data:
    enough_e = [name for name in names if name.count('e') >= 2]
    name_of_interest.extend(enough_e)
print(name_of_interest)
# wrap this whole operation up in a single nested list comprehension
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)

# flattened a list of tuples of integers into a simple list
some_tuples = [(1 , 2 , 3), (4 , 5 , 6), (7 , 8 , 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)

flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
print(flattened)

# to create a list of lists
list_of_Lists = [[x for x in tup] for tup in some_tuples]
print(list_of_Lists)










