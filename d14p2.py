# --- Day 14: Reindeer Olympics --- 
# --- Part Two ---
# 
# Seeing how reindeer move in bursts, Santa decides he's not pleased with the
# old scoring system.

# Instead, at the end of each second, he awards one point to the reindeer
# currently in the lead. (If there are multiple reindeer tied for the lead, they
# each get one point.) He keeps the traditional 2503 second time limit, of
# course, as doing otherwise would be entirely ridiculous.

# Given the example reindeer from above, after the first second, Dancer is in
# the lead and gets one point. He stays in the lead until several seconds into
# Comet's second burst: after the 140th second, Comet pulls into the lead and
# gets his first point. Of course, since Dancer had been in the lead for the 139
# seconds before that, he has accumulated 139 points by the 140th second.

# After the 1000th second, Dancer has accumulated 689 points, while poor Comet,
# our old champion, only has 312. So, with the new scoring system, Dancer would
# win (if the race ended at 1000 seconds).

# Again given the descriptions of each reindeer (in your puzzle input), after
# exactly 2503 seconds, how many points does the winning reindeer have?

import re
import fileinput

given_time = 2503

reindeers = []

class Reindeer:
    regex = re.compile(r'(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.')
    def __init__(self, line):
        reindeer, speed, time, rest = Reindeer.regex.search(line).groups()

        self.reindeer = reindeer
        # Velocitat
        self.speed = int(speed)
        # Temps que dura la velocitat
        self.time = int(time)
        # Temps de velocitat 0
        self.rest = int(rest)
        # Points
        self.points = 0

    def __str__(self):
        return '<Reindeer {}>'.format(self.reindeer)

    def __repr__(self):
        return str(self)

    # We calculate the distance for each r (reindeer) and the given t (time)
    def get_distance(self, t):
        cycles = self.time * (t/(self.time + self.rest))
        last_cycle = min(self.time, t % (self.time + self.rest))
        return self.speed * (cycles + last_cycle)

    def give_points(self):
        self.points = self.points + 1


reindeers = [Reindeer(line) for line in fileinput.input('input14')]

for t in range(1, given_time+1):
    distances = [r.get_distance(t) for r in reindeers]
    for i in range(len(reindeers)):
        if distances[i] == max(distances):
            reindeers[i].give_points()

points = [reindeer.points for reindeer in reindeers]

print max(points)