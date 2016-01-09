# --- Day 16: Aunt Sue ---

# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a
# thank you card. However, there's a small problem: she signed it "From, Aunt
# Sue".

# You have 500 Aunts named "Sue".

# So, to avoid sending the card to the wrong person, you need to figure out
# which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you
# the gift. You open the present and, as luck would have it, good ol' Aunt Sue
# got you a My First Crime Scene Analysis Machine! Just what you wanted. Or
# needed, as the case may be.

# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few
# specific compounds in a given sample, as well as how many distinct kinds of
# those compounds there are. According to the instructions, these are what the
# MFCSAM can detect:
# children, by human DNA age analysis. cats. It doesn't differentiate individual
# breeds. Several seemingly random breeds of dog: samoyeds, pomeranians, akitas,
# and vizslas. goldfish. No other kinds of fish. trees, all in one group. cars,
# presumably by exhaust or gasoline or something. perfumes, which is handy,
# since many of your Aunts Sue wear a few kinds. In fact, many of your Aunts Sue
# have many of these. You put the wrapping from the gift into the MFCSAM. It
# beeps inquisitively at you a few times and then prints out a message on ticker
# tape:

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

# You make a list of the things you can remember about each Aunt Sue. Things
# missing from your list aren't zero - you simply don't remember the value.

# What is the number of the Sue that got you the gift?

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
            raise Exception('This {} property does not exist!'.format(key))
        if value == ref[key]:
            checked += 1
    if checked == len(prop):
        print aunt_name
