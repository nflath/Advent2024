inp = [int(x) for x in open("9.in").read().strip()]

d = [-1] * sum(inp)
#print(inp)
#print(len(d))

c  = 0
ind = 0
for i in range(0, len(inp),2):
    for j in range(0, inp[i]):
        d[ind + j] = c
    c += 1
    ind += inp[i]
    if i+1 < len(inp):
        for j in range(0, inp[i+1]):
            d[ind+j] = -1
        ind += inp[i+1]
#print(d)


end = len(d) - 1
s = 0

while end != s:
    while s != end and d[s] != -1:
        s += 1
    while s != end and d[end] == -1:
        end -= 1
    if s == end:
        break
    t = d[s]
    #print('s,e',s,end)
    d[s] = d[end]
    d[end] = t
#print(d)

c = 0
for i in range(0, len(d)):
    if d[i] == -1:
        continue
    c += (i * d[i])

print(c)


starts = {}
lens  = {}
c  = 0
ind = 0

for i in range(0, len(inp),2):
    starts[c] = ind
    lens[c] = inp[i]
    for j in range(0, inp[i]):
        d[ind + j] = c

    c += 1
    ind += inp[i]
    if i+1 < len(inp):
        for j in range(0, inp[i+1]):
            d[ind+j] = -1
        ind += inp[i+1]
max_c = c - 1
s = inp[0]
assert d[s] == -1
eb = len(d)-1


for c in range (max_c, 0, -1):
    s = 0
    print(c)
    while True:
        if s >= starts[c]:
            break
        while s < len(d) and d[s] != -1:
            s += 1
        ss = s
        while ss < len(d) and d[ss] == -1 :
            ss += 1
        if s >= len(d): break
        if(ss - s) >= lens[c] and s < starts[c]:
            #print("swapped: ", s, inp[c*2])
            for i in range(s, s+inp[c*2]):
                d[i] = c
            for i in range(starts[c], starts[c]+inp[c*2]):
                d[i]  = -1
            s = s + inp[c*2]
            break
        s += 1

c = 0
for i in range(0, len(d)):
    if d[i] == -1:
        continue
    c += (i * d[i])
print(c)
