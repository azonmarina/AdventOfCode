# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#
# Santa needs help figuring out which strings in his text file are naughty or
# nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or
# aeiouaeiouaeiou. It contains at least one letter that appears twice in a
# row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd). It does not
# contain the strings ab, cd, pq, or xy, even if they are part of one of the
# other requirements. For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels
# (u...i...o...), a double letter (...dd...), and none of the disallowed
# substrings. aaa is nice because it has at least three vowels and a double
# letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel. 
#
# How many strings are nice?

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
