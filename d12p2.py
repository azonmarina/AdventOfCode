# --- Day 12: JSAbacusFramework.io ---
# 
# --- Part Two ---
# 
# Uh oh - the Accounting-Elves have realized that they double-counted everything
# red.
# 
# Ignore any object (and all of its children) which has any property with the
# value "red". Do this only for objects ({...}), not arrays ([...]).
# 
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

import json

def sum_non_reds(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if 'red' in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0
  
with open('input12') as f_in:
    print sum_non_reds(json.load(f_in))
