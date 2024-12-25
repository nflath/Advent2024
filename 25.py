inp = open("25.in").read()

locks = []
keys = []
for schematic in inp.split("\n\n"):

    s = schematic.split("\n")

    if schematic[0] == "#":
        l = []
        for i in range(0, 5):
            for j in range(1,7):
                if s[j][i] == ".":
                    l += [j - 1]
                    break
        locks += [l]
    else:
        l = []
        for i in range(0, 5):
            for j in range(1, 7):
                if s[j][i] == "#":
                    l += [5-(j - 1)]
                    break
#        print(l)
        keys += [l]
#print(locks)
#print(keys)


c = 0
for k in keys:
    for l in locks:
        good = True
#        print(k,l)
        for i in range(0, 5):
            if k[i]+l[i] > 5:
                good = False
        if good:
            c += 1
print(c)
