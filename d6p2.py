# --- Day 6: Probably a Fire Hazard ---
#
# --- Part Two ---
#
# You just finish implementing your winning light pattern when you realize you
# mistranslated Santa's message from Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each
# light can have a brightness of zero or more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of
# those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of
# those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of
# those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's
# instructions?
#
# For example:
#
# turn on 0,0 through 0,0 would increase the total brightness by 1. toggle 0,0
# through 999,999 would increase the total brightness by 2000000.

import numpy as np
import re
import fileinput
import matplotlib.pyplot as plt

order = fileinput.input('input6')

# We create the matrix of lights we want to work with
# Also, we assign the kid of data to boolean (True or False)
pretty_lights = np.zeros((1000, 1000), dtype=int)

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
    pretty_lights[coordX, coordY] += { 'off': -1, 'on': 1, 'toggle': 2 }[action]
    pretty_lights[pretty_lights < 0] = 0
    
total = sum(sum(pretty_lights))

print 'There are {} lights ON'.format(total)
plt.pcolormesh(np.array(pretty_lights), cmap='BrBG')
plt.show()

