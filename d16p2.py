# --- Day 16: Aunt Sue ---
# 
# --- Part Two ---
# 
# As you're about to send the thank you note, something in the MFCSAM's
# instructions catches your eye. Apparently, it has an outdated
# retroencabulator, and so the output from the machine isn't exact values - some
# of them indicate ranges.
# 
# In particular, the cats and trees readings indicates that there are greater
# than that many (due to the unpredictable nuclear decay of cat dander and tree
# pollen), while the pomeranians and goldfish readings indicate that there are
# fewer than that many (due to the modial interaction of magnetoreluctance).
# 
# What is the number of the real Aunt Sue?

import fileinput
import re
import json

aunts = {}    

# from this group there could be 0 or more characteristics for each aunt Sue
for line in fileinput.input('input16'):
    aunt = re.search(r'Sue (\d+): (.*)', line)
    prop = re.findall(r'(\w+): (\d+),?', aunt.group(2))
    # We create a ditctionary of each ount
    aunts[aunt.group(1)] = {}
    for pair in prop:
        # For each aunt, we create a dictionary that has its own properties
        aunts[aunt.group(1)][pair[0]] = int(pair[1])

with open('input16.json') as in16:
    # Difference between loads and load is that the first one only works with strings
    ref = json.load(in16)
    # Json makes a dictionary of the values we gave it

# We iterate so it gives us the dictionaries of properties for each aunt
for aunt_name, prop in aunts.iteritems():
    # We iterate so that for each property it gives us the value
    checked = 0
    for key, value in prop.iteritems():
        if key not in ref:
            raise Exception('{} property does not exist!'.format(key))

        if key in ['trees', 'cats']:
            if value > ref[key]:
                checked += 1
        elif key in ['pomeranians', 'goldfish']:
            if value < ref[key]:
                checked += 1
        elif value == ref[key]:
            checked += 1

    if checked == len(prop):
        print aunt_name
