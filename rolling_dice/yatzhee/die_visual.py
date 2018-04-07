from die import Die
import pygal

# Create two D6 dice.
die_1 = Die()
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

def x_labels ():
    """Creation of the list for labels."""
    x_labels = []
    x_label_min = 2

    for x_label in range(x_label_min, max_result+1):
        x_labels.append(str(x_label))

    return x_labels

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = x_labels()
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
