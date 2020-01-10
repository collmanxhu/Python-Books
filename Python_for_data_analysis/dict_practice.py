empty_dict = {}
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
print(d1)

d1[7] = 'an integer'
print(d1)
print(d1['b'])

if 'b' in d1:
    print(True)

d1[5] = 'no value'
d1['dummy'] = 'happy birthday'
print(d1)

del d1[5]
print(d1)

ret = d1.pop('dummy')
print(ret)

print(list(d1.keys()))
print(list(d1.keys()))
d1.update({'b': 'foo', 'c': 12})
print(d1)

# creating dicts from sequence, since a dict is essentially a collection of 2-tuples
key_list = ('a', 'b', 'c', 'd')
value_list = ('hello', 'oh my god', 'happy', 'data pass')
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
print(mapping)

mapping = dict(zip(range(5), reversed(range(5))))
print(mapping)

# default values
# value = some_dict.get(key, default_value)
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
# for word in words:
#     letter = word[0]
#     if letter not in by_letter:
#         by_letter[letter] = [word]
#     else:
#         by_letter[letter].append(word)
# print(by_letter)
# for word in words:
#     letter = word[0]
#     if letter not in by_letter:
#         by_letter[letter] = [word]
#         print(by_letter)
print(words[0])
print('a' in words)