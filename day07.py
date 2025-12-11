#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        data.append(list(line.rstrip()))

# part 1
diagram, splits = data[:], 0
for r in range(len(diagram) - 1):
    for c, cell in enumerate(diagram[r]):
        if cell == "S" or cell == "|":
            if diagram[r+1][c] == "^":
                splits += 1
                if c > 0:
                    diagram[r+1][c-1] = "|"
                if c < len(diagram) - 1:
                    diagram[r+1][c+1] = "|"
            else:
                diagram[r+1][c] = "|"
print(f"Splits: {splits}")

# part 2
diagram = data[:]
for i in range(len(diagram)):
    diagram[i] = [(1 if c == "S" else -1 if c == "^" else 0) for c in diagram[i]]
for r in range(len(diagram) - 1):
    for c, cell in enumerate(diagram[r]):
        if cell > 0:
            if diagram[r+1][c] == -1:
                if c > 0:
                    diagram[r+1][c-1] += cell
                if c < len(diagram) - 1:
                    diagram[r+1][c+1] += cell
            else:
                diagram[r+1][c] += cell
paths = sum(n for n in diagram[-1] if n > 0)
print(f"Paths: {paths}")