i = open("4.in")

g = i.readlines()
g = [x.strip() for x in g]
def gsearch(g, i, j, target):
    if i < 0 or i >= len(g) or j < 0 or j >= len(g[0]):
        return 0


    if g[i][j] != target[0]:
        return 0

#    print(i, j, target)

    if len(target) == 1 and g[i][j] == target:
        return 1

    c = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            c += gsearch(g, i+x, j+y, target[1:])
    return c


c = 0
for i in range(0, len(g)):
    for j in range(0, len(g[0])):
        n = gsearch(g,i,j, "XMAS")
        #if(n): print(i, j, n)
        c += n


dirs = []
for i in (1, 0, -1):
    for j in (1, 0, -1):
        if i == 0 and j == 0:
            continue
        dirs += [[i, j]]

c = 0
print(dirs)
for i in range(0, len(g)):
    for j in range(0, len(g[0])):
        for d in dirs:
            i_ = i
            j_ = j
            w = ""

            for k in range(0, 4):
                if i_ < 0 or j_ < 0 or i_ >= len(g) or j_ >= len(g):
                    continue
                w += g[i_][j_]
                i_ += d[0]
                j_ += d[1]
            if w == "XMAS":
                c += 1
print('p1',c)

c = 0
for i in range(1, len(g)-1):
    for j in range(1, len(g[0])-1):
        if g[i][j] == "A":
            o = g[i-1][j-1] + g[i+1][j+1]
            if not("M" in o and "S" in o):
                continue
            o = g[i-1][j+1] + g[i+1][j-1]
            if not("M" in o and "S" in o):
                continue
            c += 1
print("p2", c)
