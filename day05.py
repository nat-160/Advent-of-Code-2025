#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data1, data2 = ArgumentParser(), list(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    first_half = True
    for line in file:
        if not line.rstrip():
            first_half = False
        elif first_half:
            a, b = line.split("-")
            data1.append([int(a),int(b.rstrip())])
        else:
            data2.append(int(line.rstrip()))            
data1.sort()

# part 1
total = 0
for id in data2:
    for a, b in data1:
        if a <= id <= b:
            total += 1
            break
print(f"Fresh: {total}")

# part 2
total = 0
data1.sort()
for i in range(len(data1)-1,0,-1):
    if data1[i][0] <= data1[i-1][1]:
        data1[i-1][1] = max(data1[i-1][1], data1.pop(i)[1])
for a, b in data1:
    total += b - a + 1
print(f"Fresh IDs: {total}")