#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data, operations = ArgumentParser(), list(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    lines = file.readlines()
    for line in lines:
        if line[0] in ("+","*"):
            for c in line:
                if c in ("+","*"):
                    operations.append([c,0])
                else:
                    operations[-1][1] += 1
    data = [[] for _ in range(len(operations))]
    for line in lines:
        if line[0] not in ("+","*"):
            index = 0
            for i, o in enumerate(operations):
                data[i].append(line[index:index+o[1]])
                index += o[1] + 1

# part 1
total = 0
for i, o in enumerate(operations):
    op, res = lambda a, b : a + b, 0
    if o[0] == "*":
        op, res = lambda a, b : a * b, 1
    for n in data[i]:
        res = op(res, int(n))
    total += res
print(f"Total: {total}")

# part 2
total = 0
for i, o in enumerate(operations):
    op, res = lambda a, b : a + b, 0
    if o[0] == "*":
        op, res = lambda a, b : a * b, 1
    for k in range(o[1]):
        res = op(res, int("".join(data[i][j][k] for j in range(len(data[i])))))
    total += res
print(f"Fixed Total: {total}")