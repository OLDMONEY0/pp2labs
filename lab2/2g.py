from copy import copy


d = int(input())
i = 0
weak = []
while i < d:
    s = input()
    x = s.split()
    weak.append(x[1])
    i += 1
h = int(input())
hash = {}
i = 0
while i < h:
    s = input()
    x = s.split()
    e = int(x[2])
    if x[1] in hash:
        e = int(hash.get(x[1])) + e
    hash.update({x[1]: e})
    i += 1
copy = weak.copy()
for x in weak:
    if x in hash:
        e = hash.get(x)
        if e < 1:
            continue
        hash.update({x: e - 1})
        copy.remove(x)
print("Demons left:", len(copy))
