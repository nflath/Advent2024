from collections import defaultdict
inp = open("/Users/nflath/Dropbox/advent2024/2.in")

c = 0
for l in inp.readlines():
    l = [int(x) for x in l.split()]
    pos = l[1] > l[0]
    #print(l)
    safe = True
    for i in range(1, len(l)):
        if (pos and l[i] <= l[i - 1]) or (not pos and l[i] >= l[i - 1]):
            safe = False
        elif abs(l[i] - l[i - 1]) < 1 or abs(l[i] - l[i - 1]) > 3:
                safe = False
    if safe: 
        c += 1

print(c)             


c = 0
inp = open("/Users/nflath/Dropbox/advent2024/2.in")

def is_safe(l):
    pos = l[1] > l[0]
    for i in range(1, len(l)):
        if (pos and l[i] <= l[i - 1]) or (not pos and l[i] >= l[i - 1]):
            return False
        elif abs(l[i] - l[i - 1]) < 1 or abs(l[i] - l[i - 1]) > 3:
                return False
    return True

c = 0
for l in inp.readlines():
    l = [int(x) for x in l.split()]
    if is_safe(l):
         c += 1
         continue
    for i in range(0, len(l)):
         if is_safe( l[:i] + l[i+1:]):
            c += 1
            break

        

print(c)
