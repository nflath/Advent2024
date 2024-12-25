import collections,copy
inp = open("15.in")

gs,instructions = inp.read().split("\n\n")

g = {}
p = None
for i in range(0, len(gs.split("\n"))):
    for j in range(0, len(gs.split("\n")[0])):
        g[(i,j)] = gs.split("\n")[i][j]
        if g[(i,j)] == "@":
            p = (i,j)

mx = len(gs.split("\n"))
my = len(gs.split("\n")[0])

def pg():
    for i in range(0, mx):
        s = ""
        for j in range(0, my):
            s += g[(i,j)]
        print(s)
    print()

dirs = {
    "<" : (0, -1),
    ">" : (0, 1),
    "^" : (-1, 0),
    "v" : (1, 0)}


for i in instructions:
#    pg()
 #   print(i,p)
#    print(p)
    if i not in dirs: continue
    d = dirs[i]
    pp = (p[0] + d[0], p[1] + d[1])
    while g[pp] != "#":
        if g[pp] == ".":
            break
        pp = (pp[0] + d[0], pp[1] + d[1])
    if g[pp] == "#":
        continue
    #print(p, d, pp)
    p = (p[0] + d[0], p[1] + d[1])
    #print(d,p,pp)
    while g[pp] != "@":
        #print(pp, g[pp])
        g[pp] = g[(pp[0] - d[0], pp[1] - d[1])]
        pp = (pp[0] - d[0], pp[1] - d[1])
    g[pp] = "."
    #p = pp

c = 0
for i in range(0, len(gs.split("\n"))):
    for j in range(0, len(gs.split("\n")[0])):
        if g[(i,j)] == "O":
            c += (i * 100 + j)
print(c)



inp = open("15.in")
gs,instructions = inp.read().split("\n\n")
g = {}
p = None
gs = gs.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")
for i in range(0, len(gs.split("\n"))):
    for j in range(0, len(gs.split("\n")[0])):
        g[(i,j)] = gs.split("\n")[i][j]
        if g[(i,j)] == "@":
            p = (i,j)

mx = len(gs.split("\n"))
my = len(gs.split("\n")[0])

def can_move(p, d):
    moves = {}
    if d[0] == 0:
        # Normal case; don't need to worry
        pp = p
        while g[pp] != "#":
            if g[pp] == ".":
                break
            pp2 = (pp[0] + d[0], pp[1] + d[1])
            moves[pp2] = pp
            pp = pp2
#            print(pp)
        if g[pp] == "#":
            return {}
        return moves

    q = [p]
    while q:
        p, q = q[0], q[1:]
        if g[p] == "#":
            return {}
        pp = (p[0] + d[0], p[1] + d[1])
        moves[pp] = p
        if g[pp] == "#":
            return {}

        if g[pp] == "[":
            q += [pp]
            q += [(pp[0], pp[1]+1)]
        if g[pp] == "]":
            q += [pp]
            q += [(pp[0], pp[1]-1)]
    return moves

j = 0
for i in instructions:
    j += 1
    if j % 100 == 0:
        print(j)
    if i not in dirs: continue
    #print(i,)
    d = dirs[i]
    #pg()
    #print(p,d)


    moves = can_move(p, dirs[i])

    gp = copy.deepcopy(g)
    for m in moves:
        gp[m] = g[moves[m]]
        if moves[m] not in moves:
            gp[moves[m]] = "."
    g = gp
    if moves:
        g[p] = "."
        p = (p[0] + d[0], p[1] + d[1])

pg()

c = 0
for i in range(0, len(gs.split("\n"))):
    for j in range(0, len(gs.split("\n")[0])):
        if g[(i,j)] == "O":
            c += (i * 100 + j)
print(c)
