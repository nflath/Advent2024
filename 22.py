def evolve(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = (int (secret /32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret

c = 0

vals = []

for l in open("22.in").readlines():
    s = int(l)
    p = s%10
    v = []
    for i in range(2000):
        s = evolve(s)
        pp = s%10
        v += [((pp-p), pp) ]
        p = pp
    c += s
    vals += [v]
print(c)
#print(vals)


#print([x[0] for x in vals[0]])

max_c = 0

caches = []
for i in range(0, len(vals)):
    caches += [{}]


for vi in range(0, len(vals)):
    v = vals[vi]
    for m in range(0, len(v)-4):
        p = (v[m][0], v[m+1][0], v[m+2][0], v[m+3][0])
        if p in caches[vi]:
            continue
        else :
            caches[vi][p] = v[m+3][1]


for i in range(-9, 10):
    for j in range(-9, 10):
        for k in range(-9, 10):
            for l in range(-9, 10):
                p = (i,j,k,l)
                c = 0
                for v in caches:
                    if p not in v: continue
                    c += v[p]

                #if c > max_c:
                    #print(i,j,k,l)
                max_c = max(max_c, c)

print(max_c)
