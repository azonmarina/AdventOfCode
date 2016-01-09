# --- Day 15: Science for Hungry People ---

# Today, you set out on the task of perfecting your milk-dunking cookie recipe.
# All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
# list of the remaining ingredients you could use to finish the recipe (your
# puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk) durability (how well it
# keeps the cookie intact when full of milk) flavor (how tasty it makes the
# cookie) texture (how it improves the feel of the cookie) calories (how many
# calories it adds to the cookie) You can only measure ingredients in whole-
# teaspoon amounts accurately, and you have to be accurate so you can reproduce
# your results in the future. The total score of a cookie can be found by adding
# up each of the properties (negative totals become 0) and then multiplying
# together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3 Then,
# choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
# (because the amounts of each ingredient must add up to 100) would result in a
# cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76

# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now)
# results in a total score of 62842880, which happens to be the best score
# possible given these ingredients. If any properties had produced a negative
# total, it would have instead become zero, causing the whole score to multiply
# to zero.

# Given the ingredients in your kitchen and their properties, what is the total
# score of the highest-scoring cookie you can make?

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
    return np.prod(properties[:-1])

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
# We extract using the regex all the values from the int
ingredients = np.fromregex('input15', regex, np.int)

# max_score = -1e32
# for spoons in split(len(ingredients), 100):
#     max_score = max(score(spoons, ingredients), max_score)
# print 'The best cookie will have a value of {} units.'.format(max_score)

# We calculate the scores given the number of spoons for each ingredient (split spoons for ingredient)
scores = [score(spoons, ingredients) for spoons in split(len(ingredients), 100)]

print 'The best cookie will have a value of {} units.'.format(max(scores))
