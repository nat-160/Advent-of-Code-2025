#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for pID in file.readline().split(','):
        f, l = pID.split('-')
        data.append((int(f),int(l.rstrip())))

# part 1
total = 0
for f, l in data:
    for n in range(f, l+1):
        id = str(n)
        i = len(id) // 2
        if id[:i] == id[i:]:
            total += n
print(f"Total: {total}")

# part 2
total = 0
for f, l in data:
    for n in range(f, l+1):
        id = str(n)
        for i in range(len(id) // 2, 0, -1):
            if len(id) % i:
                continue
            seq, adding = id[:i], True
            for j in range(len(id)//i):
                if id[j*i:(j+1)*i] != seq:
                    adding = False
                    break
            if adding:
                total += n
                break
print(f"New Total: {total}")