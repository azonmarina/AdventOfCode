# --- Day 4: The Ideal Stocking Stuffer ---
# --- Part 2 ---
# Now find one that starts with six zeroes.


import hashlib

password = 'bgvyzdsv' 

i = 0
answer = ''

while not answer.startswith('000000'):
    i += 1
    answer = hashlib.md5(password + str(i)).hexdigest()

print(i)
