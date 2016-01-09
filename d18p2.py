# --- Day 18: Like a GIF For Your Yard ---

# --- Part Two ---

# You flip the instructions over; Santa goes on to point out that this is all
# just an implementation of Conway's Game of Life. At least, it was, until you
# notice that something's wrong with the grid of lights you bought: four lights,
# one in each corner, are stuck on and can't be turned off. The example above
# will actually run like this:

# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#

# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####

# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###

# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#

# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#

# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#
# After 5 steps, this example now has 17 lights on.

# In your grid of 100x100 lights, given your initial configuration, but with the
# four corners always in the on state, how many lights are on after 100 steps?


# These need to stay on.
corners = {(0,0), (0,99), (99,0), (99,99)}
with open('input18') as f:
    # Set up the board (use set union to make sure corners are on)
    lights = corners | { (x,y) for y, line in enumerate(f)
                        for x, char in enumerate(line.strip())
                        if char == '#' }

# This returns the number of neighbours that are turned on.
# The _ means in python "all the values that meet these conditions" more or less.
neighbours = lambda x,y: sum((_x,_y) in lights for _x in (x-1, x, x+1)
                            for _y in (y-1, y, y+1) if (_x, _y) != (x, y))

# Do 100 iterations
for c in xrange(100):
    # Calculate new 'lights' from previous one, use a set union to make sure coners are turned 'on'
    lights = corners | { (x,y) for x in xrange(100) for y in xrange(100)
                        if (x,y) in lights and 2 <= neighbours(x,y) <= 3
                        or (x,y) not in lights and neighbours(x,y) == 3 }
print len(lights)
