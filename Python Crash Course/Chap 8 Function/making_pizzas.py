import pizza1

pizza1.make_pizza(10, 'pepermini')
pizza1.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza1 import make_pizza
make_pizza(10,'pepermini')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza1 import make_pizza as mp
mp(16,'pepermini')
mp(14, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
import pizza1 as p
p.make_pizza(15,'pepermini')
p.make_pizza(13, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
from pizza1 import *
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')