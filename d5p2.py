# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# --- Part Two ---
#
# Realizing the error of his ways, Santa has switched to a better model of
# determining whether a string is naughty or nice. None of the old rules
# apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the
# string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
# aaa (aa, but it overlaps). It contains at least one letter which repeats
# with exactly one letter between them, like xyx, abcdefeghi (efe), or even
# aaa. For example:
#
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a
# letter that repeats with exactly one letter between them (zxz). xxyxx is
# nice because it has a pair that appears twice and a letter that repeats with
# one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a
# single letter between them. ieodomkazucvgmuy is naughty because it has a
# repeating letter with one between (odo), but no pair that appears twice. How
# many strings are nice under these new rules?

import fileinput

nice = 0
forbidden = ['ab', 'cd', 'pq', 'xy']

for line in fileinput.input("input5"):

    # Children who curse are naughty
    # if ('ab' or 'cd' or 'pq' or 'xy') in line:
    
    n_curse = 0
    for bad in forbidden:
        if bad in line:
            n_curse += 1

    n_vowel = 0
    n_rep = 0
    last_char = ''

    for char in line:
        # Children who don't use enough vowels are naughty
        if char in 'aeiou':
            n_vowel += 1
        # Children who don't repeat letters are naughty
        if last_char == char:
            n_rep += 1
        # Update Last Char to the actual one for next interation  
        last_char = char

    if n_vowel >= 3 and n_rep >= 1 and n_curse < 1:
        nice += 1

    # else:
        # print line
        # print 'n_vowel {} and n_rep {}\n'.format(n_vowel, n_rep)


print "There are {} nice children this year".format(nice)
