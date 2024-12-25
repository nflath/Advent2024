import collections

l = open("11.in").read().split()

for step in range(0, 25):
   #print(step)
   n = []
   for i in l:
       if i == "0":
           n += ["1"]
       elif len(i) % 2 == 0:
           n += [i[0:int(len(i)/2)]]
           n += [str(int(i[int(len(i)/2):]))]
       else:
           n += [ str(int(i)*2024) ]
   l = n
#print(n)
print(len(n))

j = open("11.in").read().split()

l = collections.defaultdict(int)
for i in j:
    l[i] += 1

for s in range(0, 75):
    nl = collections.defaultdict(int)
    for i in l:
        if i == "0":
            nl["1"] += l[i]
        elif len(i) % 2 == 0:
            nl[i[0:int(len(i)/2)]] += l[i]
            nl[str(int(i[int(len(i)/2):]))] += l[i]
        else:
            nl[str(int(i)*2024)] += l[i]
    l = nl


c = 0
for i in l:
    c += l[i]
print(c)
