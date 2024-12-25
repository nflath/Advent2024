from functools import lru_cache
import collections
towels = []
patterns = []

for l in open("19.in").readlines():
    l = l.strip()
    if not l: continue
    if not towels:
        towels = l.split(", ")
    else:
        patterns += [l]


prefix = collections.defaultdict(set)

for towel in towels:
    for i in range(0, len(towel)+1):
        prefix[towel[:i]].add(towel)

#print(towels)
#print(prefix)
@lru_cache(maxsize=None)
def can_construct(pattern):
    if not pattern: return 1
    c = 0
    v = set()
    for i in range(1,len(pattern)+1,1):
        towels = prefix[pattern[:i]]
        if not towels:
            #print(pattern, c, pattern[:i])
            return c
        for towel in towels:
            if towel in v: continue
            if pattern[:len(towel)] == towel:
#                print("Adding: ", can_construct(pattern[len(towel):]), pattern[:len(towel)], towel)
                v.add(towel)
                c += can_construct(pattern[len(towel):])
    #print(pattern, c)
    return c


c = 0
c2 = 0
for pattern in patterns:
    print(pattern,can_construct(pattern))
    if can_construct(pattern):
        c += 1
    c2 += can_construct(pattern)
print(c,c2)
