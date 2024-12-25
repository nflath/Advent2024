import collections

inp = open("24.in")

vars, eqs = inp.read().split("\n\n")

r = {}
for l in vars.split("\n"):
    l = l.strip()
    v, v2 = l.split(": ")
    r[v] = int(v2)
#    print(v,v2)

c = True
while c:
    c = False
    for l in eqs.split("\n"):
        l = l.strip()
        #print("l",l)

        if "AND" in l:
            vars, result = l.split(" -> ")
            v1, v2 = vars.split(" AND ")
#            print("RESULT",result)
            if v1 not in r or v2 not in r:
                c = True
                continue
            r[result] = r[v1] & r[v2]
        elif "XOR" in l:
            vars, result = l.split(" -> ")
            v1, v2 = vars.split(" XOR ")
            if v1 not in r or v2 not in r:
                c = True
                continue
            r[result] = r[v1] ^ r[v2]
        elif "OR" in l:
            vars, result = l.split(" -> ")
            v1, v2 = vars.split(" OR ")
            if v1 not in r or v2 not in r:
                c = True
                continue
            r[result] = (r[v1] | r[v2])
        else:
            assert False
print(r)

varz = ""
v = 0
for i in range(100, -1, -1):
    varz = "z{:02d}".format(i)
#    print("w",varz, varz in r)
    if varz not in r:
        continue
    #print(varz, r[varz])
    v = (v << 1) + r[varz]

print(v)
