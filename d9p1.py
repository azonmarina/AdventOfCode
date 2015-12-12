# --- Day 9: All in a Single Night ---
# 
# --- Part 1 ---
# 
# Every year, Santa manages to deliver all of his presents in a single night.
# 
# This year, however, he has some new locations to visit; his elves have
# provided him the distances between every pair of locations. He can start and
# end at any two (different) locations he wants, but he must visit each location
# exactly once. What is the shortest distance he can travel to achieve this?
# 
# For example, given the following distances:
# 
# London to Dublin = 464 London to Belfast = 518 Dublin to Belfast = 141 The
# possible routes are therefore:
# 
# Dublin -> London -> Belfast = 982 
# London -> Dublin -> Belfast = 605 
# London -> Belfast -> Dublin = 659 
# Dublin -> Belfast -> London = 659 
# Belfast -> Dublin -> London = 605 
# Belfast -> London -> Dublin = 982 
# 
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
# 
# What is the distance of the shortest route?

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

min_distance = (min(path(towns, distances) for towns in itertools.permutations(distances)))

print 'The minimum distance we will need is {} some measure'.format(min_distance)



