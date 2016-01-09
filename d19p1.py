# --- Day 19: Medicine for Rudolph ---

# Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly,
# and he needs medicine.

# Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph
# is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer
# chemistry isn't similar to regular reindeer chemistry, either.

# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission
# plant, capable of constructing any Red-Nosed Reindeer molecule you need. It
# works by starting with some input molecule and then doing a series of
# replacements, one per step, until it has the right molecule.

# However, the machine has to be calibrated before it can be used. Calibration
# involves determining the number of molecules that can be generated in one step
# from a given starting point.

# For example, imagine a simpler machine that supports only the following
# replacements:

# H => HO
# H => OH
# O => HH

# Given the replacements above and starting with HOH, the following molecules
# could be generated:

# HOOH (via H => HO on the first H).
# HOHO (via H => HO on the second H).
# OHOH (via H => OH on the first H).
# HOOH (via H => OH on the second H).
# HHHH (via O => HH).

# So, in the example above, there are 4 distinct molecules (not five, because
# HOOH appears twice) after one replacement from HOH. Santa's favorite molecule,
# HOHOHO, can become 7 distinct molecules (over nine replacements: six from H,
# and three from O).

# The machine replaces without regard for the surrounding characters. For
# example, given the string H2O, the transition H => OO would result in OO2O.

# Your puzzle input describes all of the possible replacements and, at the
# bottom, the medicine molecule for which you need to calibrate the machine. How
# many distinct molecules can be created after all the different ways you can do
# one replacement on the medicine molecule?

from string import replace
from random import shuffle
from re import findall

# We create a list with all the molecules
replacements = [a for a in findall(r'(\w+) => (\w+)',open('input19').read())]

src = open('input19').readlines()[-1]

dest = set()

for replacement in replacements:
    # j is pointing to the start of the unprocessed part of the string
    i = 0
    j = 0
    while replacement[0] in src[j:]:
        # find next place we can replace
        i = src[j:].index(replacement[0])
        # add to the set
        dest.add(src[:j + i] + replacement[1] + src[j + i + len(replacement[0]):])
        # update the search start pointer
        j = j + len(replacement[0])

print len(dest)

# sort replacements by length of replacement
replacements = sorted(replacements, key = lambda x: len(x[1]))[::-1]

a = 0
replaces = 0
src_bak = src
# greedily try the replacements from longest to shortest until we arrive at e (hopefully, or any 1 length result)
while len(src) > 1:
    if replacements[a][1] in src:
        replaces += src.count(replacements[a][1])
        src = replace(src, replacements[a][1], replacements[a][0])
        a = 0
    else:
        a += 1
    # Randomize replacements until we succeed!!
    if a > len(replacements)-1:
        src = src_bak
        shuffle(replacements)
        a = 0
        replaces = 0

print replaces
