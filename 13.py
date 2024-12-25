
inp = open("13.in").read().split("\n\n")

import sympy as sp
from sympy.abc import x, y, z
from sympy.solvers import solve,nsolve



# 8400 = 94A + 22B
c = 0
for l in inp:
    #print(l)
    as_,bs,ps = l.split("\n")

    a = eval("(" + as_.replace("Button A: X+","").replace("Y+","") + ")")
    b = eval("(" + bs.replace("Button B: X+","").replace("Y+","") + ")")
    p = eval("(" + ps.replace("Prize: X=","").replace("Y=","") + ")")
#    print(a,b,p)

    for i in range(0, 100):
        t = p
        t = (t[0] - a[0] * i, t[1] - a[1] * i)


        xt = ((t[0] / b[0]))
        yt = ((t[1] / b[1]))

        if xt != int(xt) or yt != int(yt) or xt != yt:
            continue
        else:
            c += (i * 3 + xt)
print(c)

#94 * A + 22 * B = 8400
# A = (8400 - 22B) / 94

# 34 * A + 67 * B = 5400
# 34 * (8400 - 22B) / 94 + 67 * B = 5400
# (-22 * 34)B/94 + 67 B = 5400 - 34 * 8400 / 94

c = 0
for l in inp:
    as_,bs,ps = l.split("\n")

    a = eval("(" + as_.replace("Button A: X+","").replace("Y+","") + ")")
    b = eval("(" + bs.replace("Button B: X+","").replace("Y+","") + ")")
    p = eval("(" + ps.replace("Prize: X=","").replace("Y=","") + ")")
    p = (p[0] + 10000000000000, p[1] + 10000000000000)
    #print(a,b,p)
    #print(a[0] * 80 + b[0] * 40)
    #print(a[1] * 80 + b[1] * 40)
    s = solve([a[0] * x + b[0] * y - p[0], a[1] * x + b[1] * y - p[1]], (x,y), dict=True)[0]
    if s[x] == int(s[x]) and s[y] == int(s[y]):
        c += (3 * s[x] + s[y])
print(c)
