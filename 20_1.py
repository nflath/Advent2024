import collections

g = {}
i = 0
s = None
e = None

for l in open("20.in").readlines():

    for j in range(0, len(l)):
        g[(i,j)] = l[j]
        if l[j] == "S":
            s = (i,j)
        if l[j] == "E":
            e = (i,j)

    i+=1
bounds = (i,j)


dirs = [(1,0), (-1,0), (0, 1), (0, -1)]

distances = {}
def find_distances(t):
    q = [(t, 0)]
    while q:
        p, c = q[0]
        q = q[1:]

        if p in distances:
            continue
        distances[p] = c

        for d in dirs:
            pp = (p[0] + d[0], p[1] + d[1])
            if g[pp] != "#":
                q += [(pp, c+1)]

find_distances(e)
target_score = distances[s]
print(target_score)
saved = collections.defaultdict(int)

def find_cheats():
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if (i,j) not in distances:
                continue
            for k in range(-2, 3):
               for l in range(-2, 3):
                   if abs(k)+abs(l) != 2:
                       continue
                   if (i+k,j+l) not in distances:
                       continue
                   if distances[(i+k,j+l)] < (distances[(i,j)]):
                       saved[distances[(i,j)]-distances[(i+k,j+l)]-(abs(k)+abs(l))] += 1


find_cheats()

c = 0
for s in saved:
    #print(s, saved[s])
    if s >= 100:
        c += saved[s]
print(c)

cheats = set()

saved = collections.defaultdict(int)
def find_cheats_2():
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if (i,j) not in distances:
                continue
            for k in range(-20, 21):
               for l in range(-20, 21):
                   if abs(k)+abs(l) > 20:
                       continue
                   if (i+k,j+l) not in distances:
                       continue
                   if distances[(i+k,j+l)] < (distances[(i,j)]+(abs(k)+abs(l))):
                       saved[distances[(i,j)]-distances[(i+k,j+l)]-(abs(k)+abs(l))] += 1


find_cheats_2()
print("Part 2")
c = 0
for s in saved:
    if s >= 100:
        c += saved[s]
print(c)


# def bfs(s, t):
#     q = [(s, 0)]
#     v = set()
#     while q:
#         p, c = q[0]
#         q = q[1:]

#         if p in v:
#             continue
#         if p == t:
#             return c
#         v.add(p)

#         for d in dirs:
#             #print(p)
#             pp = (p[0] + d[0], p[1] + d[1])
#             if g[pp] != "#":
#                 q += [(pp, c+1)]

# target_score = bfs(s, e)
# print('ts:',target_score)
# def bfs_c(s, t, target_score):
#     saved = collections.defaultdict(int)
#     q = [(s, (), 0)]

#     v = set()

#     c_ = 0

#     while q:
#         p, cheats, c = q[0]
#         if c_ != c:
#             print(c, len(q))
#             c_ = c
#         q = q[1:]

#         if c > target_score:
#             continue

#         if (p,cheats) in v:
#             continue
#         if (p, ()) in v:
#             continue

#         if cheats == 0 and g[p] == "#":
#             continue

#         if p == t:
#             saved[target_score-c] += 1

#         v.add((p,cheats))

#         for d in dirs:
#             pp = (p[0] + d[0], p[1] + d[1])
#             if not(pp[0] >= 0 and pp[1] >= 0 and pp[0] < bounds[0] and pp[1] < bounds[1]):
#                 continue
#             if g[pp] != "#":
#                 q += [(pp, cheats, c+1)]
#             elif len(cheats) == 1:
#                 q += [(pp, (cheats[0], pp) , c+1)]
#             elif len(cheats) == 0:
#                 q += [(pp, (pp) , c+1)]
#     return saved

# saved = bfs_c(s, e, target_score)
# c = 0
# for s in saved:
#     print(s, saved[s])
#     if s >= 100:
#         c += saved[s]
