#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        data.append([c=='@' for c in line.rstrip()])

# part 1
total, n, m = 0, len(data), len(data[0])
for r, row in enumerate(data):
    for c, pos in enumerate(row):
        if pos:
            adjacent = 0
            for i in (-1,0,1):
                for j in (-1,0,1):
                    if 0<=r+i<n and 0<=c+j<m and (i!=j or i!=0) and data[r+i][c+j]:
                        adjacent += 1
            if adjacent < 4:
                total += 1
print(f"Accessible: {total}")

# part 2
total, removed = 0, 1
while removed:
    removed = 0
    for r, row in enumerate(data):
        for c, pos in enumerate(row):
            if pos:
                adjacent = 0
                for i in (-1,0,1):
                    for j in (-1,0,1):
                        if 0<=r+i<n and 0<=c+j<m and (i!=j or i!=0) and data[r+i][c+j]:
                            adjacent += 1
                if adjacent < 4:
                    total += 1
                    data[r][c] = False
                    removed += 1
    
print(f"Removable: {total}")
