# --- Part Two ---

# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:

# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?
# import fileinput

floor = 0
first = True

# For fileinput.input we read each line of our file
for line in fileinput.input("input1"):
    #For each line we read each element in the file
    #We use enumerate so it returns a 2 Tuple with the position (step) and the value in line
    for step,i in enumerate(line):
        if i == "(":
            floor = floor + 1
        else:
            floor = floor - 1
        if floor == -1 and first:
            print "the position of the user is {}".format(step+1)
            first = False

    print "floor's number is {}".format(floor)
