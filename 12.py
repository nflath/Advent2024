#  755027 7 too low
import collections
g_ = [[y for y in x.strip()  ] for x in open("12.in").readlines()]

g = collections.defaultdict()

for i in range(0, len(g_)):
    for j in range(0, len(g_[0])):
        g[(i,j)] = g_[i][j]

v = set()

price = 0
dirs = ( (1,0), (-1, 0), (0, 1), (0, -1) )

def bfs(g, v, start):
    target = g[start]
    q = [start]

    area = 0
    perimeter = 0
    sides = set()
    vv = set()
    while q:
        p = q[0]
        q = q[1:]
        if p in v:
            continue
        v.add(p)
        vv.add(p)
        area += 1

        for d in dirs:
            p_ = (p[0] + d[0], p[1] + d[1])
            if p_ in g and g[p_] == target:
                q += [p_]
            else:
                sides.add(p_)
                perimeter += 1
    #print(target, area, perimeter, num_sides(vv, sides))
    return area, perimeter, num_sides(vv, sides)


def num_sides(vvv, sides):
    vv = set()

    r = 0
    #print(sides)

    for p in sides:
        if p in vv: continue

        ds = set()

        n = 0
        for d in dirs:
            if (p[0] + d[0], p[1] + d[1]) in vvv and (p[0] + d[0], p[1] + d[1]) :
                ds.add(d)
        #print(p, len(ds))
#        print(p, n)
#        r += n

        vv.add(p)
        for d in dirs:
            p_ = (p[0] + d[0], p[1] + d[1])
            while p_ not in vv and p_ in sides:
                vv.add(p_)
                p_ = (p_[0] + d[0], p_[1] + d[1])

                #for d2 in dirs:
                    #if (p_[0] + d2[0], p_[1] + d2[1]) in vvv:
                        #ds.add(d2)
                #if p_ in vvv:
                    #ds.add(d)

        r += len(ds)
    return r


price2 = 0
for i in range(0, len(g_)):
    for j in range(0, len(g_[0])):

        if (i, j) not in v:
            a, p, sides = bfs(g, v, (i, j))
            price += a * p
            price2 += a * sides
            print(g[(i,j)],a,p,sides)

print(price, price2)



import collections
g_ = [[y for y in x.strip()  ] for x in open("12.in").readlines()]

g = collections.defaultdict()

for i in range(0, len(g_)):
    for j in range(0, len(g_[0])):
        g[(i,j)] = g_[i][j]

v = set()

price = 0
dirs = ( (1,0), (-1, 0), (0, 1), (0, -1) )

def bfs(g, v, start):
    target = g[start]
    q = [start]

    area = 0
    perimeter = 0
    sides = set()
    vv = set()
    while q:
        p = q[0]
        q = q[1:]
        if p in v:
            continue
        v.add(p)
        vv.add(p)
        area += 1

        for d in dirs:
            p_ = (p[0] + d[0], p[1] + d[1])
            if p_ in g and g[p_] == target:
                q += [p_]
            else:
                sides.add(p_)
                perimeter += 1

    for (x,y) in vv:
        pass

    return area, perimeter, num_sides(vv, sides)

def part2(puzzle_input):
    grid = puzzle_input.split()
    m = len(grid)
    n = len(grid[0])

    def get_corners(i, j):
        NW, W, SW, N, S, NE, E, SE = [
            is_same(i+x, j+y, grid[i][j])
            for x in range(-1, 2)
            for y in range(-1, 2)
            if x or y
        ]
        return sum([
            N and W and not NW,
            N and E and not NE,
            S and W and not SW,
            S and E and not SE,
            not (N or W),
            not (N or E),
            not (S or W),
            not (S or E)
        ])

    def is_same(i, j, plant):
        return (
            i in range(m) and
            j in range(n) and
            grid[i][j] == plant
        )

    def find_region(i, j):
        plant = grid[i][j]
        region = set()
        queue = set([(i, j)])
        while queue:
            i, j = queue.pop()
            region.add((i, j))
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if (is_same(x, y, plant) and
                    (x, y) not in region and
                    (x, y) not in queue
                ):
                    queue.add((x, y))

        corners = sum(get_corners(x, y) for x, y in region)
        return region, corners * len(region)

    total = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region, cost = find_region(i, j)
                total += cost
                visited |= region

    return total

print(part2(open("12.in").read()))
