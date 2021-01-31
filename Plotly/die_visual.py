from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D8s
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list
results = [die_1.roll() * die_2.roll() for roll_num in range(10_000)]

# Analyse the results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualise results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 10000 times and multiplying them together', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6^2.html')
