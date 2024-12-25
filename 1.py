from collections import defaultdict
inp = open("/Users/nflath/Dropbox/advent2024/1.in")

l = [[], []]
for line in inp.readlines():
    l[0] += [int(line.split()[0])]
    l[1] += [int(line.split()[1])]


l[0] = sorted(l[0])
l[1] = sorted(l[1])

c = 0
for i in range(0, len(l[0])):
     c += abs(l[0][i] - l[1][i])

print(c)               

# Part 2

counts =  [ defaultdict(int), defaultdict(int) ]

for i in range(0, len(l[0])):
    counts[0][l[0][i]] += 1
    counts[1][l[1][i]] += 1

c = 0

for i in range(0, len(l[0])):
    c += l[0][i] * counts[1][l[0][i]]

print(c)
