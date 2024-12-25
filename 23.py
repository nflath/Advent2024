import collections
inp = open("23.in")
nodes = collections.defaultdict(set)

for l in inp.readlines():
    a,b = l.strip().split("-")
    nodes[a].add(b)
    nodes[b].add(a)

overall_visited = set()

triples = set()

for node in nodes:
    for neighbor in nodes[node]:
        for nn in nodes[neighbor]:
            if nn in nodes[node]:
                t = tuple(sorted([node, neighbor, nn]))
                triples.add(t)

c = 0
for t in triples:
    if [x for x in t if x[0] == "t"]:
        c += 1

print(len(triples))
print(c)


connecteds = triples

`owhile True:
    print len(connecteds)
    new_connecteds = set()
    for component in connecteds:
        for n in nodes:
            if n in component: continue
            in_all = True
            for c in component:
                if n not in nodes[c]:
                    in_all = False
                    break
            if in_all:

                new_connecteds.add ( tuple(sorted( list(component) + [n])))
    if not new_connecteds:
        break
    connecteds = new_connecteds

assert len(connecteds) == 1
print(connecteds)
for c in connecteds:
    print(",".join(c))
