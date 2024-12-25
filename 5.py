inp = open("5.in").readlines()

os = []
ps = []
for l in inp:
    if "|" in l:
        os += [[int(x) for x in l.split("|")]]
    if "," in l:
        ps += [ [int(x) for x in l.split(",")] ]

c = 0

ios = []
eps = []
for p in ps:
    g = True
    for o in os:
        if o[0] in p and o[1] in p:
            if not(p.index(o[0]) < p.index(o[1])):
#                print(p, o)
                g = False
    if g:
        c += p[int(len(p)/2)]
    else:
        eps += [p]
print(c)

#print(os)
c = 0
#print(eps)
for p in eps:
    changed = True
    while changed:
      changed = False
      for o in os:
        if o[0] in p and o[1] in p:
            if not(p.index(o[0]) < p.index(o[1])):
                i = p.index(o[1])
                j = p.index(o[0])
                t = p[i+1]
                #print(p,o,i,j,t)
                p[i] = o[0]
                p[i+1] = o[1]
                if i+ 1 != j:
                    p[j] = t
                changed = True
    c += p[int(len(p)/2)]
    #break

print(eps)

print(c)
