import pygal
from die import Die

die = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die.roll() + die_2.roll() + die_3.roll()
    results.append(result)


frequencies = []
max_result = die.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling three D6 1000 times."
hist.x_labels = [x for x in range(3,19)]
hist._x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('Two D6 dices',frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)