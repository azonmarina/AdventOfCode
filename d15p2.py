# --- Day 15: Science for Hungry People ---

# --- Part Two ---

# Your cookie recipe becomes wildly popular! Someone asks if you can make
# another recipe that has exactly 500 calories per cookie (so they can use it as
# a meal replacement). Keep the rest of your award-winning process the same (100
# teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40
# teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to
# 100), the total calorie count would be 40*8 + 60*3 = 500. The total score
# would go down, though: only 57600000, the best you can do in such trying
# circumstances.

# Given the ingredients in your kitchen and their properties, what is the total
# score of the highest-scoring cookie you can make with a calorie total of 500?

import re
import numpy as np

# Calculates the total score given the number of spoons for each ingredient
def score(spoons, ingredients):
    # We calculate each property with the number of spoons we have 
    # for each ingredient
    properties = (ingredients.T*spoons).sum(axis=1)
    # If we have a negative value, then we make it 0
    properties[properties < 0] = 0
    # We multiply the properties we have for the cookie (tuple style)
    return np.prod(properties[:-1]), properties[-1]

# Splits the number of spoons for each possible ingredient
def split(sums, n):
    if sums == 1:
        yield (n, )
    else:
        # being xrange the number of spoons we can have
        for a in range(n+1):
            # Calling the function in the function... WOOOOAH!
            for rest in split(sums-1, n-a):
                # Yield is the same as return, but it returns a Generator 
                # (it only calculates it once)
                yield ((a, ) + rest)

regex = r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)'
# We extract using the regex all the values from the string that are ints
ingredients = np.fromregex('input15', regex, np.int)

# We calculate the scores given the number of spoons for each ingredient (split spoons for ingredient)
scores = (score(spoons, ingredients) for spoons in split(len(ingredients), 100))

print 'The best cookie will have a value of {} units with no more than 500 calories.'.format(max(score 
    for score, calories in scores if calories == 500))


