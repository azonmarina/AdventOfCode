# --- Day 9: All in a Single Night --- #  --- Part Two ---
# 
# The next year, just to show off, Santa decides to take the route with the
# longest distance instead.
# 
# He can still start and end at any two (different) locations he wants, and he
# still must visit each location exactly once.
# 
# For example, given the distances above, the longest route would be 982 via
# (for example) Dublin -> London -> Belfast.
# 
# What is the distance of the longest route?

from collections import defaultdict
import itertools
import fileinput
import re

def path(towns, distances):
    distance = 0
    for town1, town2 in zip(towns, towns[1:]):
        # We add up the distances from each town to the next one according to the permutation
        distance += distances[town1][town2]
    return distance

distances = defaultdict(dict)

for line in fileinput.input('input9'):
    # We look for the data from each line in the file
    town1, town2, distance = re.search('^(\w+) to (\w+) = (\d+)$', line).groups()
    # We create a matrix of distances for each town
    distances[town1][town2] = int(distance)
    distances[town2][town1] = int(distance)

min_distance = (max(path(towns, distances) for towns in itertools.permutations(distances)))

print 'The minimum distance we will need is {} some measure'.format(min_distance)



