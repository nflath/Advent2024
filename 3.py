import re

r = re.compile("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
i = open("3.in").read()

m_ = re.findall(r, i)
c = 0
yes = True
for m in m_:
    if m[1]: yes = True
    if m[2]: yes = False

    if m[0] and yes:
        m = eval(m[0][4:-1])
        c += (m[0] * m[1])
print(c)
