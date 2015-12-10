# --- Day 7: Some Assembly Required --- #  
# 
# --- Part Two ---
# 
# Now, take the signal you got on wire a, override wire b to that signal, and
# reset the other wires (including wire a). What new signal is ultimately
# provided to wire a?

import fileinput
import re

# NAMESPACE
# We will create a dictionary with the known signals that will be added later on
wires = {}

# LOOKUP TABLE (it's the table where we look up the command we will need)
gates = {
    'AND'   : lambda x,y: x & y,
    'OR'    : lambda x,y: x | y,
    'LSHIFT': lambda x,y: x << y,
    'RSHIFT': lambda x,y: x >> y,
    'NOT'   : lambda x,y: ~ y,
    ''      : lambda x,y: y
}

# Constant with the Regular expression that parses the Input File
regex = re.compile(r'^(\w*?)\s*([A-Z]*?)\s*(\w+)\s+->\s+(\w+)$')

lineinput = fileinput.input('input7')

for line in lineinput:
    # We transform our string line into a tuple pretty list
    in1, op, in2, out = regex.search(line).groups()
    # We write the OUT result from GATES in the namespace of WIRE
    # We create a function that "saves up" what to do when we get all the values ready
    # We apply the concept of CLOSURE. Because in1 and in2 are immutable, we can use the
    # original values and have new ones.
    wires[out] = {'in1': in1, 'in2': in2, 'op': op, 'done': False, 'out': -1}


def getOutput(wireName):
    # We have a collection of wires and we look for wireName using indexation
    # w = wanted Wire
    w = wires[wireName]

    # print w

    if w['done']:
        return w['out']

    opWW = w['op']

    in1WW = int(w['in1']) if w['in1'].isdigit() else (getOutput(w['in1']) if w['in1'] else '')
    in2WW = int(w['in2']) if w['in2'].isdigit() else (getOutput(w['in2']) if w['in2'] else '')

    output = gates[opWW](in1WW, in2WW)

    w['out'] = output
    w['done'] = True

    return output

# We find the first ouptut for 'a'
a = getOutput('a')

# We reset the values in 'done' in all the wires
for w in wires.values():
    w['done'] = False

# We change the values in 'b' for the already saved values of the first 'a'
wires['b']['op'] = ''
wires['b']['in2'] = str(a)

# We calculate the signal in 'a' again
target = 'a'
print 'The signal in wire {} is {}'.format(target, getOutput(target))
