# --- Day 11: Corporate Policy ---

# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has
# devised a method of coming up with a password based on the previous one.
# Corporate policy dictates that passwords must be exactly eight lowercase
# letters (for security reasons), so he finds his new password by incrementing
# his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so
# on. Increase the rightmost letter one step; if it was z, it wraps around to a,
# and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has
# imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like
# abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't
# count. Passwords may not contain the letters i, o, or l, as these letters can
# be mistaken for other characters and are therefore confusing. Passwords must
# contain at least two different, non-overlapping pairs of letters, like aa, bb,
# or zz. For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

import re
from string import ascii_lowercase as lowercase

re_pairs = r'(.)\1.*(.)\2'

def create_next_letters():
    # Remember 'z' case is different than the rest!
    pairs = zip(lowercase, lowercase[1:])
    mapping = {c1: c2 for c1, c2 in pairs}
    # How to hardcoded skip the invalid letters
    mapping['h'] = 'j'
    mapping['n'] = 'p'
    mapping['k'] = 'm'

    return mapping

def substrings(s, lenght=1):
    # We generate all the desired length substrings of 's'
    # yields : str: substrings of s
    for i in range(len(s) - lenght):
        yield s[i:i + lenght]

def valid(password):
    if not re.search(re_pairs, password):
        return False
    return any(s in lowercase for s in substrings(password, 3))

def next_string(s, next_letters):
    # get first string without invalid letters
    # increase first invalid letter and reset everything after to 'a's
    s = re.sub( r'([iol])(\w*)', lambda m: next_letters[m.group(1)] + 'a' * len(m.group(2)), s)

    if s[-1] == 'z':
        return next_string(s[:-1], next_letters) + 'a'
    else:
        return s[:-1] + next_letters[s[-1]]

def next_valid_password(password, next_letters):
    while True:
        password = next_string(password, next_letters)
        if valid(password):
            return password


password_in = 'hxbxwxba'
next_letters = create_next_letters()

password_out = next_valid_password(password_in, next_letters)
print 'The next password to {} is {}'.format(password_in, password_out)