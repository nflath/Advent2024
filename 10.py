g = [[int(y) if y != '.' else -1 for y in x.strip()  ] for x in open("10.in").readlines()]

def inbounds(g, i, j):
    return i >= 0 and j >= 0 and i < len(g) and j < len(g[0])


trailheads = set()

for i in range(0, len(g)):
    for j in range(0, len(g[0])):
        if g[i][j] == 0:
            trailheads.add( (i,j) )

dirs = [ (0,1), (0, -1), (1,0), (-1, 0) ]

c = 0
for t in trailheads:

    v = set()
    q = [t]

    while q:
        p = q[0]
        q = q[1:]

        for d in dirs:
            if g[p[0]][p[1]] == 9:
                v.add(p)
            np = (p[0] + d[0], p[1] + d[1])
            if inbounds(g, np[0], np[1]) and g[np[0]][np[1]] == (g[p[0]][p[1]] + 1):
                q += [np]
    c += len(v)

print(c)


c = 0
print(trailheads)
for t in trailheads:

    v = set()
    q = [t]
    n = 0
    while q:
        p = q[0]
        q = q[1:]
        #print(p, g[p[0]][p[1]])

        if g[p[0]][p[1]] == 9:
            n += 1


        for d in dirs:

            np = (p[0] + d[0], p[1] + d[1])
            if inbounds(g, np[0], np[1]) and g[np[0]][np[1]] == (g[p[0]][p[1]] + 1):
                q += [np]
    #print(t, n)
    c += n

print(c)
