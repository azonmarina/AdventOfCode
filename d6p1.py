# --- Day 6: Probably a Fire Hazard ---
#
# Because your neighbors keep defeating you in the holiday house decorating
# contest year after year, you've decided to deploy one million lights in a
# 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has mailed
# you instructions on how to display the ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights
# at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions
# include whether to turn on, turn off, or toggle various inclusive ranges
# given as coordinate pairs. Each coordinate pair represents opposite corners
# of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore
# refers to 9 lights in a 3x3 square. The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights
# by doing the instructions Santa sent you in order.
#
# For example:
#
# turn on 0,0 through 999,999 would turn on (or leave on) every light. 
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning
# off the ones that were on, and turning on the ones that were off. 
# turn off 499,499 through 500,500 would turn off (or leave off) the middle
# four lights. 
# 
# After following the instructions, how many lights are lit?

import numpy as np
import re
import fileinput
import matplotlib.pyplot as plt

order = fileinput.input('input6')

# We create the matrix of lights we want to work with
# Also, we assign the kid of data to boolean (True or False)
pretty_lights = np.zeros((1000, 1000), dtype=bool)

# Pretty function to analyse the order we have been given and extract the important data!
def analOrder(order):
    # We create a list with all the data that is relevant to us using Regular Expressions
    [action, x0, y0, x1, y1] = re.search('(\w+) (\d+),(\d+) through (\d+),(\d+)', order).groups()

    x0 = int(x0)
    x1 = int(x1) + 1
    y0 = int(y0)
    y1 = int(y1) + 1

    # What do we want from this function? The result! The integers inside () create a tuple on its own.
    return action, slice(x0, x1), slice(y0, y1)

for line in order:
    action, coordX, coordY = analOrder(line)
    if action == 'toggle':
        pretty_lights[coordX, coordY] ^= 1
    else:
        pretty_lights[coordX, coordY] = ['off', 'on'].index(action)

total = sum(sum(pretty_lights))

print 'There are {} lights ON'.format(total)
plt.pcolormesh(np.array(pretty_lights), cmap='BrBG')
plt.show()

