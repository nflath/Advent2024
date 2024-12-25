import collections
t = (6,6)


m = 1024
t = (70,70)

i = 0
g = collections.defaultdict(int)
for l in open("18.in").readlines():
    if i == m:
        break
    g[eval(l)] = 1
    i += 1

# for i in range(0 ,t[0]+1):
#     s = ""
#     for j in range(0, t[1]+1):
#         s += str(g[(j,i)])
#     print(s)


q = [((0,0), 0)]


dirs = [(1,0), (-1,0), (0,1), (0,-1)]

v = set()
while q:
    p, c = q[0]
    q = q[1:]
    if p in v:
        continue
    if p == t:
        break

    v.add(p)

    for d in dirs:
        pp = (p[0] + d[0], p[1] + d[1])
        if pp[0] >= 0 and pp[1] >= 0 and pp[0] < (t[0]+1) and pp[1] < (t[1]+1) and g[pp] == 0:
            q += [(pp, c+1)]
print(c)
