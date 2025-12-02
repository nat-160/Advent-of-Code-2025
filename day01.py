#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        r, n = line[0], int(line.rstrip()[1:])
        data.append((r,n))

# part 1
dial, count = 50, 0
for r, n in data:
    dial += n * (-1 if r == 'L' else 1)
    dial %= 100
    if dial == 0:
        count += 1
print(f"Password: {count}")

# part 2
dial, count = 50, 0
for r, n in data:
    for _ in range(n):
        dial += 1 if r == 'R' else -1
        if dial == 100:
            dial = 0
        elif dial == -1:
            dial = 99
        if dial == 0:
            count += 1
print(f"New Password: {count}")