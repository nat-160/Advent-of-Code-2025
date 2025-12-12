#!/usr/bin/env python3

# load input
from argparse import ArgumentParser
p, data = ArgumentParser(), list()
p.add_argument('filename')
with open(p.parse_args().filename, "r") as file:
    for line in file:
        x, y, z = line.rstrip().split(",")
        data.append((int(x),int(y),int(z)))

# part 1
def dist(a, b):
    return (a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2 + (a[2]-b[2]) ** 2
distances, n = list(), len(data)
for i in range(n - 1):
    for j in range(i + 1, n):
        distances.append((dist(data[i], data[j]), i, j))
distances.sort()
pt2 = distances[:] # for pt 2
groups, members = [False] * n, dict()
for i in range(10 if n == 20 else 1000):
    _, a, b = distances.pop(0)
    if groups[a] and groups[b]:
        if groups[a] != groups[b]:
            old_key = groups[b]
            members[groups[a]].update(members[old_key])
            for member in members[old_key]:
                groups[member] = groups[a]
            del members[old_key]
    elif groups[a]:
        groups[b] = groups[a]
        members[groups[a]].add(b)
    elif groups[b]:
        groups[a] = groups[b]
        members[groups[b]].add(a)
    else: 
        key = str(a) + ":" + str(b)
        members[key] = {a, b}
        groups[a] = groups[b] = key
largest = [1, 1, 1]
for group in members.values():
    largest.append(len(group))
    largest.sort()
    largest.pop(0)
product = largest[0] * largest[1] * largest[2]
print(f"Product: {product}")

# part 2
distances = pt2
groups, members = [False] * n, dict()
while not members or len(next(iter(members.values()))) != len(data):
    _, a, b = distances.pop(0)
    if groups[a] and groups[b]: 
        if groups[a] != groups[b]:
            old_key = groups[b]
            members[groups[a]].update(members[old_key])
            for member in members[old_key]:
                groups[member] = groups[a]
            del members[old_key]
    elif groups[a]: 
        groups[b] = groups[a]
        members[groups[a]].add(b)
    elif groups[b]: 
        groups[a] = groups[b]
        members[groups[b]].add(a)
    else:
        key = str(a) + ":" + str(b)
        members[key] = {a, b}
        groups[a] = groups[b] = key
    product = data[a][0] * data[b][0]
print(f"Product: {product}")