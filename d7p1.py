# --- Day 7: Some Assembly Required ---
# 
# --- Part 1 ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic
# gates! Unfortunately, little Bobby is a little under the recommended age
# range, and he needs help assembling the circuit.
# 
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit
# signal (a number from 0 to 65535). A signal is provided to each wire by a
# gate, another wire, or some specific value. Each wire can only get a signal
# from one source, but can provide its signal to multiple destinations. A gate
# provides no signal until all of its inputs have a signal.
# 
# The included instructions booklet describes how to connect the parts together:
# x AND y -> z means to connect wires x and y to an AND gate, and then connect
# its output to wire z.
# 
# For example:
# 
# 123 -> x means that the signal 123 is provided to wire x. x AND y -> z means
# that the bitwise AND of wire x and wire y is provided to wire z. p LSHIFT 2 ->
# q means that the value from wire p is left-shifted by 2 and then provided to
# wire q. NOT e -> f means that the bitwise complement of the value from wire e
# is provided to wire f. Other possible gates include OR (bitwise OR) and RSHIFT
# (right-shift). If, for some reason, you'd like to emulate the circuit instead,
# almost all programming languages (for example, C, JavaScript, or Python)
# provide operators for these gates.
# 
# For example, here is a simple circuit:
# 
# 123 -> x 456 -> y 
# x AND y -> d 
# x OR y -> e 
# x LSHIFT 2 -> f 
# y RSHIFT 2 -> g
# NOTx -> h 
# NOT y -> i 
# 
# After it is run, these are the signals on the wires:
# 
# d: 72 
# e: 507 
# f: 492 
# g: 114 
# h: 65412 
# i: 65079 
# x: 123 
# y: 456 
# 
# In little Bobby's kit's instructions booklet (provided as your puzzle 
# input), what signal is ultimately provided to wire a?

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

# ------ CHEEKY-LITTLE-BASTARD WAY --
# for line in lineinput:
#
#     # We map our line and separate both sides of the line (operation -- result)
#     line = map(lambda s: s.strip(), line.split('->'))
#     # All of them have the same value, so we replace the text for the expressions
#     # Nice discovery from friendly Stackoverflow... we can all do it in just one looooong line!
#     wire[line[1].upper()] = line[0].replace('AND', '&').replace('OR', '|').replace('NOT ', '~').replace('RSHIFT', '>>').replace('LSHIFT', '<<').upper()
#
# for i in range(340):
#     for val, expr in wire.iteritems():
#         try:
#             exec(val + ' = (' + expr + ') & 65535')
#         except Exception:
#             pass
# --------------------------

target = 'a'

print 'The signal in wire {} is {}'.format(target, getOutput(target))
