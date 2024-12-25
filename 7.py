def f(target, running, vals):
    if running > target:
        return False
    if len(vals) == 0 and target == running:
        return True
    if len(vals) == 0:
        return False
    return f(target, running + vals[0], vals[1:]) or f(target, running * vals[0], vals[1:]) or f(target, int(str(running) + str(vals[0])), vals[1:])

c = 0
for l in open("7.in").readlines():
    target = int(l.split(":")[0])
    vals = [int(x) for x in l.split(":")[1].split()]
    if f(target, vals[0], vals[1:]):
        c += target
print(c)
