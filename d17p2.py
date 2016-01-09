# --- Day 17: No Such Thing as Too Much ---
# 
# --- Part Two ---
# 
# While playing with all the containers in the kitchen, another load of eggnog
# arrives! The shipping and receiving department is requesting as many
# containers as you can spare.
# 
# Find the minimum number of containers that can exactly fit all 150 liters of
# eggnog. How many different ways can you fill that number of containers and
# still hold exactly 150 litres?
# 
# In the example above, the minimum number of containers was two. There were
# three ways to use that many containers, and so the answer there would be 3.

import fileinput
from itertools import combinations

lines = []

for line in fileinput.input('input17'):
    lines.append(int(line))
s=0
ans = 0

for k in range(len(lines)):
    for c in combinations(lines, k):
        if sum(c) == 150:
            ans += 1
    if ans:
        break
print ans