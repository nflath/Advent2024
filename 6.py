dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

g = [x.strip() for x in open("6.in").readlines()]
ps = set()
p = ()

d = 0
#print(g)
for i in range(0, len(g)):
    for j in range(0, len(g[0])):
        if g[i][j] == "^":
            p = (i,j)


op = p
while p[0] >= 0 and p[0] < len(g) and p[1] >= 0 and p[1] < len(g[0]):
    ps.add(tuple(p))
    np = (p[0]+dirs[d][0], p[1] + dirs[d][1])
    if not (np[0] >= 0 and np[0] < len(g) and np[1] >= 0 and np[1] < len(g[0])):
        p = np
        continue
    if g[np[0]][np[1]] == "#":
        d = (d + 1) % 4
#        print(p), dirs[d]
    else:
        p = np
print(len(ps))        

g = [ [ y for y in x] for x in g]
#for x in g:
#    print(x)
count = 0
for p in ps:
 #   print(p, len(g), len(g[p[0]]))
#    print(g[p[0]][p[1]])
    p_ = p
    d = 0
    if p == op: continue
    g[p[0]][p[1]] = '#'
    p = op
    v = set()
    while p[0] >= 0 and p[0] < len(g) and p[1] >= 0 and p[1] < len(g[0]):
        np = (p[0]+dirs[d][0], p[1] + dirs[d][1])
        if not (np[0] >= 0 and np[0] < len(g) and np[1] >= 0 and np[1] < len(g[0])):
            p = np
            continue
#        print (np, g[np[0]][np[1]])
        if g[np[0]][np[1]] == "#":
#            print(p,d)
            d = (d + 1) % 4
        else:
            if (p,d) in v:
#                print(p)
                count += 1
                break
            v.add( (p,d) )
            p = np
    g[p_[0]][p_[1]] = '.'
print(count)
    
    
