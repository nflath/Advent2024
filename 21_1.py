import collections

keypad_ = [x for x in """789
456
123
 0A""".split("\n")]
#print(keypad_)
keypad = {}
for i in range(0, len(keypad_)):
    for j in range(0, len(keypad_[i])):
        keypad[(i,j)] = keypad_[i][j]



directional_=[x for x in """ ^A
<v>""".split("\n")]
directional = {}
for i in range(0, len(directional_)):
    for j in range(0, len(directional_[i])):
        directional[(i,j)]= directional_[i][j]

#print(directional)

a_location_d = (0,2)
a_location_k = (3,2)

position = ( (0,2), (0,2), (3,2))


dirs = {
    "<" : (0,-1),
    ">" : (0,1),
    "^" : (-1, 0),
    "v" : (1, 0)
    }
#print(directional)
#print(keypad)

def in_bounds_d(pp):
    return not (pp[0] < 0 or pp[1] < 0 or pp[0] > 1 or pp[1] > 2 or (pp[0] == 0 and pp[1] == 0))

def in_bounds_k(pp):
    return not (pp[0] < 0 or pp[1] < 0 or pp[0] > 3 or pp[1] > 2 or (pp[0] == 3 and pp[1] == 0))

#print(in_bounds_k( (0,2)))
#for i in range(0, 2):
    #for j in range(0, 4):
        #print((i,j), in_bounds_d( (i,j)))

def bfs(position, target):
    q = [(position, "", target)]

    v = set()

    while q:
        p, path, remainder = q[0]
        if remainder == "":
            return path
        q = q[1:]

        if (p, remainder) in v:
            continue
        v.add((p, remainder))

        for dir in ["<",">","v","^","A"]:
            if dir == "A":
                if p[0] == a_location_d:
                    if p[1] == a_location_d:
                        if keypad[p[2]] == remainder[0]:
                            q += [ (p, path + "A", remainder[1:]) ]
                        else:
                            continue
                    else:
                        inner_dir = directional[pp[1]]
                        pp = (p[0], p[1], (p[2][0] + dirs[inner_dir][0], p[2][1] + dirs[inner_dir][1]))
                        if not in_bounds_k(pp[2]):
                            continue
                        q += [(pp, path+"A", remainder)]
                else:
                    inner_dir = directional[p[0]]
                    pp = (p[0], (p[1][0] + dirs[inner_dir][0], p[1][1] + dirs[inner_dir][1]), p[2])
                    if not in_bounds_d(pp[1]):
                        continue
                    q += [(pp, path+dir, remainder)]
            else:
                pp = ((p[0][0] + dirs[dir][0], p[0][1] + dirs[dir][1]), p[1], p[2])
                if not in_bounds_d(pp[0]):
                    continue
                q += [ (pp, path + dir, remainder) ]

#print(directional)
c = 0
for line in open("21.in").readlines():
    position = ( (0,2), (0,2), (3,2))
    path = bfs(position, line.strip())
    #print("line:",path, len(path), int(line.strip()[:-1]))
    c += len(path) * int(line.strip()[:-1])
print(c)



inp = open("21.in")


key_fastest = collections.defaultdict(set)

def bfs_k(s, t):
    if not in_bounds_k(s) or not in_bounds_k(t):
        return None
    q = [(s,"")]
    v = set()
    new_q = []
    retn = set()
    while q:
        while q:
            p,path = q[0]
            q = q[1:]
            for dir in ["<",">","v","^","A"]:
                if dir == "A":
                    if keypad[t] == keypad[p]:
                        retn.add(path)
                else:
                    pp = (p[0] + dirs[dir][0], p[1] + dirs[dir][1] )
                    if not in_bounds_k(pp):
                        continue
                    new_q += [ (pp, path+dir) ]
        if len(retn): return retn
        q = new_q
        new_q = []

directional_fastest = collections.defaultdict(set)
def bfs_d(s, t):
    if not in_bounds_d(s) or not in_bounds_d(t):
        return None

    retn = set()
    q = [(s,"")]
    v = set()
    new_q = []
    while q:
        while q:
            p,path = q[0]
            q = q[1:]
            #if p in v and t != directional[p]: continue
            v.add(p)
            for dir in ["<",">","v","^","A"]:
                if dir == "A" :
                    if directional[t] == directional[p]:
                        retn.add(path)
                    continue
                else:
                    pp = (p[0] + dirs[dir][0], p[1] + dirs[dir][1] )
                    if not in_bounds_d(pp):
                        continue
                    new_q += [ (pp, path+dir) ]
        if len(retn):
            return retn
        q = new_q
        new_q = []

for i in range(0, len(keypad_)):
    for j in range(0, len(keypad_[0])):
        for k in range(0, len(keypad_)):
            for l in range(0, len(keypad_[0])):
                if (i,j) in keypad and (k,l) in keypad:
                    key_fastest[ (keypad[(i,j)], keypad[(k,l)]) ] = bfs_k((i,j),(k,l))

for i in range(0, len(directional_)):
    for j in range(0, len(directional_[0])):
        for k in range(0, len(directional_)):
            for l in range(0, len(directional_[0])):
                if (i,j) in directional and (k,l) in directional:
                    directional_fastest[ (directional[(i,j)], directional[(k,l)]) ] = bfs_d((i,j),(k,l))


pos = [(0,2)] * 25 + [(3,2)]



for key in directional_fastest:
    best = None
    if directional_fastest[key] is None:
        continue
    for possibility in directional_fastest[key]:
        if not best or len(expand(best)) > len(possibility): best = possibility
    directional_fastest[key] = set()
    directional_fastest[key] = best

for key in key_fastest:
    best = None
    if key_fastest[key] is None:
        continue
    for possibility in key_fastest[key]:
        if not best or len(expand(best)) > len(possibility): best = possibility
    key_fastest[key] = best




for l in open("21.in").readlines():
    l = l.strip()
    p = collections.defaultdict(int)

    from = "A"
    for c in l:
        for j in key_fastest_(A):
            p[j] += 1







print(c)


#print(key_fastest)
