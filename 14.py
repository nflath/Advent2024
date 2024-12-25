import collections
robots = []
for l in open("14.in").readlines():
    robots += [ (eval("(" + l[2:l.find("v")] + ")"), eval("(" + l[l.find("v")+2:] + ")")) ]

p = []
s = 100

mx = 101
my = 103
for r in robots:
    p += [ ((r[0][0] + r[1][0] * 100) % mx, (r[0][1] + r[1][1] * 100) % my) ]

#print(p)
def q(p):
    if p[0] < (mx/2 - 1) and p[1] < (my/2 - 1):
        return 1
    if p[0] > (mx/2) and p[1] < (my/2 - 1):
        return 2
    if p[0] < (mx/2 - 1) and p[1] > (my/2):
        return 3
    if p[0] > (mx/2) and p[1] > (my/2):
        return 4


c = collections.defaultdict(int)
for r in p:
    c[q(r)] += 1
def s(c):
    return c[4] * c[1] * c[2] * c[3]

print(c[4] * c[1] * c[2] * c[3])

ms = s(c)
mi = 100
p = [r[0] for r in robots]
for t in range(0, 20000):

    for i in range(0, len(robots)):
        p[i] = ((robots[i][0][0] + robots[i][1][0] * t) % mx,
                (robots[i][0][1] + robots[i][1][1] * t) % my)

#    print(p)
#    break
    if len(p) == len(set(p)):
        print(t)

    c = collections.defaultdict(int)
    for r in p:
        c[q(r)] += 1
    s_ = s(c)
    if s_ < ms:
        ms = s_
        mi = t
print(mi)

# 8886 too high
