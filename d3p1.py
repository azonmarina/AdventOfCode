# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to
# move next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present to the
# house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a little off, and Santa ends up visiting some
# houses more than once. How many houses receive at least one present?
#
# For example:
#
# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

import fileinput


for line in fileinput.input('input3'):
    location = [0,0]
    houses = set()
    #For each line we read each element in the file
    for i in line:
        if i == '^':
            location[0] = location[0] + 1
        elif i == 'v':
            location[0] = location[0] - 1
        elif i == '>':
            location[1] = location[1] + 1
        elif i == '<':
            location[1] = location[1] - 1

        # Since the values are mutable, we want them unmutable for the set()
        # function. Else, it does not like it because they can be changed,
        # making it hard.
        t = tuple(location)

        houses.add(t)

    print len(houses)