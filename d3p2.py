# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
# --- Part Two ---
#
# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to
# the same starting house), then take turns moving based on instructions from
# the elf, who is eggnoggedly reading from the same script as the previous
# year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-
# ^Santa goes south. >v< now delivers presents to 3 houses, and Santa and
# ^Robo-Santa end up back where they started. v^v^v^v^v now delivers presents
# ^to 11 houses, with Santa going one direction and Robo-Santa going the
# ^other.

import fileinput


for line in fileinput.input('input3'):
    loc_santa = [0,0]
    loc_robot = [0,0]
    houses_santa = set()
    houses_robot = set()
    #For each line we read each element in the file
    for position,i in enumerate(line):
        if position % 2 == 0:
            if i == '^':
                loc_santa[0] = loc_santa[0] + 1
            elif i == 'v':
                loc_santa[0] = loc_santa[0] - 1
            elif i == '>':
                loc_santa[1] = loc_santa[1] + 1
            elif i == '<':
                loc_santa[1] = loc_santa[1] - 1
        else:
            if i == '^':
                loc_robot[0] = loc_robot[0] + 1
            elif i == 'v':
                loc_robot[0] = loc_robot[0] - 1
            elif i == '>':
                loc_robot[1] = loc_robot[1] + 1
            elif i == '<':
                loc_robot[1] = loc_robot[1] - 1

        # Since the values are mutable, we want them unmutable for the set()
        # function. Else, it does not like it because they can be changed,
        # making it hard.
        t_santa = tuple(loc_santa)
        t_robot = tuple(loc_robot)

        houses_santa.add(t_santa)
        houses_robot.add(t_robot)
        
    #Union is made here because then we do not have to do it in every cicle,
    #making the code waaaay faster
    houses = houses_santa.union(houses_robot)
    print len(houses)