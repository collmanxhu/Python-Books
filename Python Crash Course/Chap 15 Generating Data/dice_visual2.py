# 15-9 Die Comprehensions: rewrite the iteration loops

import plotly.graph_objects as go
from plotly import offline

from die import Die

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for _ in range(50000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
x_values = list(range(2, max_result+1))
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title='Results of rolling a D6 and a Die10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

data = [go.Bar(x=x_values, y=frequencies)]
fig = go.Figure(data, my_layout)
fig.show()

# offline.plot({'data': data, 'layout': my_layout},
#              filename='d6.html')