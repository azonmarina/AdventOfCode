
# --- Day 13: Knights of the Dinner Table ---
# 
# --- Part Two ---
# 
# In all the commotion, you realize that you forgot to seat yourself. At this
# point, you're pretty apathetic toward the whole thing, and your happiness
# wouldn't really go up or down regardless of who you sit next to. You assume
# everyone else would be just as ambivalent about sitting next to you, too.
# 
# So, add yourself to the list, and give all happiness relationships that
# involve you a score of 0.
# 
# What is the total change in happiness for the optimal seating arrangement that
# actually includes yourself?

import re
import itertools
import fileinput

INPUT = fileinput.input('input13')
re_guests = re.compile(r'(.*) would (.*) (\d*) happiness units by sitting next to (\w*).')
# Compile dictionary from given input
d = {}
for line in INPUT:
    partner1, gainlose, h, partner2 = re_guests.search(line).groups()
    h = int(h)
    if gainlose == 'lose':
        # We make the value of happiness negative because it is sadness
        h *= -1
    # 'distance' of happiness between the guests
    d[(partner1, partner2)] = h

# Part 2
# Iterate through permutations (all the possibilites)
partners = {k[0] for k in d.keys()}
for n in partners:
    d[(n, 'Me')] = 0
    d[('Me', n)] = 0

partners.add('Me')
# -- End Part 2 --

seatings = itertools.permutations(partners)

# No seats = no happy... let's change that!
max_happiness = 0

for seating in seatings:

    happiness = 0

    happiness += d[(seating[-1], seating[0])]
    happiness += d[(seating[0], seating[-1])]
    for i in range(0, len(seating)-1):
            happiness += d[(seating[i], seating[i+1])]
    for i in range(1, len(seating)):
            happiness += d[(seating[i], seating[i-1])]

    if happiness > max_happiness:
        max_happiness = happiness

print'The maximum happiness this table can possibly have is {}. Weeee!'.format(max_happiness)