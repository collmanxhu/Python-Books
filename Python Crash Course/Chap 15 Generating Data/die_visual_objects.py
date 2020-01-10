import plotly.graph_objects as go
from plotly import offline

from die import Die

# Create two D6 dice
die = Die()

# Make some rolls, and store results in a list
results = [die.roll() for _ in range(1000)]

# Analyze the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results
x_values = list(range(1, die.num_sides+1))
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

data = [go.Bar(x=x_values, y=frequencies)]
fig = go.Figure(data, my_layout)
fig.show()

# offline.plot({'data': data, 'layout': my_layout},
#              filename='d6.html')