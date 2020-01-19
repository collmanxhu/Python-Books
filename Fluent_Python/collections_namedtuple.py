"""
Standard tuple uses numerical indexes to access its members which can lead to errors,
especially if the tuple has a lot of fields. namedtuple assigns names, as well as the
numerical index, to each member.

amedtuple instances are just as memory efficient as regular tuples because they do not
have per-instance dictionaries. Each kind of namedtuple is represented by its own class,
created by using the namedtuple() factory function. The arguments are the name of the new
class and a string containing the names of the elements.
"""

import collections
import sys

PPPerson = collections.namedtuple('Participant', 'name age gender')
bob = PPPerson(name='Bob', age=35, gender='male')
print(bob)
print(bob.gender)

# Invalid Field Names : As the field names are parsed, invalid values cause ValueError exceptions.

try:
    collections.namedtuple('Person', 'name class age gender')
except ValueError:
    tb = sys.exc_info()[1]
    print(tb)
    # print(ValueError)

try:
    collections.namedtuple('Person', 'name age age gender')
except ValueError:
    tb = sys.exc_info()[1]
    print(tb)

# In situations where a namedtuple is being created based on values outside of the control
# of the program (such as to represent the rows returned by a database query, where the
# schema is not known in advance), set the rename option to True so the fields are renamed.
with_class = collections.namedtuple('Person', 'name class age gender', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age gender age', rename=True)
print(two_ages._fields)