import collections
g_ = [x.strip() for x in open("16.in").readlines()]

e = None
s = None
r = None

g = {}

dirs = {
    (0, 1) : ((1, 0), (-1, 0)),
    (0, -1) : ((1, 0), (-1, 0)),
    (1, 0) : ((0, 1), (0, -1)),
    (-1, 0) : ((0, 1), (0, -1)),
    }

for i in range(0, len(g_)):
    for j in range(0, len(g_[i])):
        g[(i,j)] = g_[i][j]
        if g_[i][j] == "E":
            e = (i, j)
        if g_[i][j] == "S":
            g[(i,j)]= "."
            r = ( (i,j),  (0, 1) )

#print(e,"r=",r)

min_score = {}
min_score_pt = {}

prev = {}

def dfs(s):
    c = None
    q = [(s, 0, None)]
    v = set()
    while q:
        p, score, prev_node = q[0]
        q = q[1:]
        if p in v and min_score[p] < score:
            continue
        if p not in min_score or score < min_score[p]:
            prev[p] = set()
        prev[p].add(prev_node)

        min_score[p] = score
        v.add(p)
        if p[0] == e and (not c or c > score):
            c = score
            #print(c)

        pos, dir = p
        pp = (pos[0] + dir[0], pos[1] + dir[1])
        if g[pp] == "#":
            pass
        else:
            q += [((pp, dir), score + 1, p)]

        for d in dirs[dir]:

            q += [((pos, d), score + 1000, p)]
    return c


# 101492
print(dfs(r))

nodes_in_path = set()
q = [r[0]]
#for q in prev:
    #print(q, prev[q])

#print("E:",e,prev[e])

correct_target = (e, (0,1))

for d in dirs:
    if min_score[(e, d)] < min_score[correct_target]:
        correct_target = (e, d)

q = [correct_target]
while q:
    p, q = q[0], q[1:]
    if p is None:
        continue
    #print("Adding",p,"prev:",prev[p])
    nodes_in_path.add(p[0])
    if p not in prev:
        continue
    for pp in prev[p]:
        q += [pp]

print(correct_target)

print(len(nodes_in_path))

# for i in range(0, len(g_)):
#     s = ""
#     for j in range(0, len(g_[0])):
#         if (i,j) in nodes_in_path:
#             s += "O"
#         else:
#             s += g[(i,j)]

#     print(s,)
