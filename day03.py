#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        data.append(line.rstrip())

# part 1
total = 0
for bank in data:
    first, last = 0, 1
    for i in range(1, len(bank)-1):
        if bank[i] > bank[first]:
            first, last = i, i + 1
        elif bank[i] > bank[last]:
            last = i
    if bank[-1] > bank[last]:
        last = -1
    total += int(bank[first]+bank[last])
print(f"Joltage: {total}")

# part 2
total = 0
for bank in data:
    joltage, start = "0", 0
    for i in range(12):
        best = start
        for j in range(start, len(bank) - 11 + i):
            if bank[j] > bank[best]:
                best = j
            if bank[best] == '9':
                break
        start, joltage = best + 1, joltage + bank[best]
    total += int(joltage)
print(f"New Joltage: {total}")