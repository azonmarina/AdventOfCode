# --- Day 11: Corporate Policy ---
# 
# --- Part Two ---
# 
# Santa's password expired again. What's the next one?

import re
from string import ascii_lowercase as lowercase

# If we compile all the regex before, we will save up time!
re_pairs = re.compile(r'(.)\1.*(.)\2')
re_next = re.compile(r'([iol])(\w*)')

def create_next_letters():
    # Remember 'z' case is different than the rest!
    pairs = zip(lowercase, lowercase[1:])
    mapping = {c1: c2 for c1, c2 in pairs}
    # How to hardcoded skip the invalid letters
    mapping['h'] = 'j'
    mapping['n'] = 'p'
    mapping['k'] = 'm'

    return mapping

def substrings(s, length=1):
    # We generate all the desired length substrings of 's'
    # yields : str: substrings of s
    for i in range(len(s) - length):
        yield s[i:i + length]

def valid(password):
    if not re_pairs.search(password):
        return False
    return any(s in lowercase for s in substrings(password, 3))

def next_string(s, next_letters):
    # get first string without invalid letters
    # increase first invalid letter and reset everything after to 'a's
    s = re_next.sub(lambda m: next_letters[m.group(1)] + 'a' * len(m.group(2)), s)

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

password_out1 = next_valid_password(password_in, next_letters)
password_out2 = next_valid_password(password_out1, next_letters)
print 'The next password to {} is {}'.format(password_out1, password_out2)