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

import string
import fileinput


def nicey(evil_kid, pair):
    n_pair_kid = 0
    now = 1

    while now < len(evil_kid):
        if (evil_kid[now-1] + evil_kid[now]) == pair:
            n_pair_kid += 1

        if  now < (len(evil_kid)-1) and evil_kid[now-1] == evil_kid[now] and evil_kid[now] == evil_kid[now+1]:
            now += 1
        now += 1
    return n_pair_kid > 1
            


myList = []
# We create all the possible pairs in the alphabet
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        pair = i + j
        # In other languages, instead of append it normally is push
        myList.append(pair)


santa_log = fileinput.input('input5')
nice = 0

for line in santa_log:
    n_pair = False
    for pair in myList:
        if nicey(line,pair):
            n_pair = True
            break

    n_rep = False
    if len( [x for x in zip(line[:-2], line[2:]) if x[0] == x[1]] ) > 0:
        n_rep = True

    if n_pair and n_rep:
        nice += 1

print 'There are {} nice kids'.format(nice)
