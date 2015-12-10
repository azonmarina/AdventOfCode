####### THE PRETTY WAY #######
import string
import fileinput


def nicey(evil_kid, pair):
    n_pair_kid = 0
    now = 1

    while now < len(evil_kid):
        if (evil_kid[now-1] + evil_kid[now]) == pair:
            n_pair_kid += 1

        if  now < (len(evil_kid)-1) and evil_kid[now-1] == evil_kid[now] and evil_kid[now] == evil_kid[now+1]:
            now += 1
        now += 1
    return n_pair_kid > 1


santa_log = fileinput.input('input5')
nice = 0

for line in santa_log:

    ########## POSSIBLE (BUT NOT WORKING) SUPER PRETTY WAY ###########
    # n_pair = any([line[i:i+1] in line[i+2:] for i in range(len(line)-2)])
    ##################################################################

    #We create a list of tuples with all the possible pairs in the line
    pairs = zip(line[:-1], line[1:])

    # We have to create the list of pairs, so we sum them up from the list 'pairs'
    newpair = map(lambda x: x[0] + x[1], pairs)

    # We try each possible pair in newpair in line
    # My lonely option
    for pair in newpair:
        n_pair = nicey(line,pair)
        if n_pair:
            break

    # Option 10003040404050
    # n_pair = any([nicey(line, pair) for pair in newpair])
    # Option 20203040506006
    # n_pair = any(map(lambda pair: nicey(line, pair), newpair))

    n_rep = len( [x for x in zip(line[:-2], line[2:]) if x[0] == x[1]] ) > 0

    if n_pair and n_rep:
        nice += 1


print 'There are {} nice kids'.format(nice)
            