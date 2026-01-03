#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, rows, cols = ArgumentParser(), list(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        c, r = line.split(",")
        rows.append(int(r))
        cols.append(int(c))

# part 1
area = lambda t: (abs(t[0]-t[2])+1) * (abs(t[1]-t[3])+1)
squares = list((rows[i], cols[i], rows[j], cols[j]) for i in range(len(rows)-1) for j in range(i+1, len(rows)))
squares.sort(key = area, reverse = True)
print("Largest area:", area(squares[0]))

# part 2
lines = list((rows[i-1], cols[i-1], rows[i], cols[i]) for i in range(len(rows)))
def intersects(s, l): 
    if min(l[0], l[2]) < max(s[0], s[2]):
        if min(l[1], l[3]) < max(s[1], s[3]):
            if max(l[0], l[2]) > min(s[0], s[2]):
                if max(l[1], l[3]) > min(s[1], s[3]):
                    return True
for s in squares:
    valid = True
    for l in lines:
        if intersects(s, l):
            valid = False
            break
    if valid:
        print("Largest valid area:", area(s))
        break