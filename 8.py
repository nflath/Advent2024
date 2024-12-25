import collections
g = [x.strip() for x in open("8.in").readlines()]

antennas = collections.defaultdict(set)
for i in range(0, len(g)):
    for j in range(0, len(g[0])):
        if g[i][j] != '.':
            antennas[g[i][j]].add((i,j))

antinodes = set()

for a in antennas:
    for a1 in antennas[a]:
        for a2 in antennas[a]:
            if a1 == a2: continue
            id = a1[0] - a2[0]
            jd = a1[1] - a2[1]

            antinodes.add( (a1[0] - 2 *id, a1[1] - 2 *jd) )
            antinodes.add( (a1[0] + id, a1[1] + jd))

antinodes_real = set()
antinodes = set([x for x in antinodes if x[0] >= 0 and x[1] >= 0 and x[0] < len(g) and x[1] < len(g[0])])
print(len(antinodes))

antinodes = set()


for a in antennas:
    for a1 in antennas[a]:
        for a2 in antennas[a]:
            if a1 == a2: continue
            id = a1[0] - a2[0]
            jd = a1[1] - a2[1]

            mul = 0
            while True:
                p = (a1[0] - (mul + 1) *id, a1[1] - (mul + 1) *jd)
                if p[0] < 0 or p[1] < 0 or p[0] >= len(g) or p[1] >= len(g[0]):
                    break
                else:
                    antinodes.add( p)
                    mul += 1
            mul = 0
            while True:
                p = (a1[0] + (mul *id), a1[1] + (mul *jd))
                if p[0] < 0 or p[1] < 0 or p[0] >= len(g) or p[1] >= len(g[0]):
                    break
                else:
                    antinodes.add( (p))
                    mul += 1


print(len(antinodes))
