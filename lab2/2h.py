x, y = map(int, input().split())
a = int(input())
d = []
i = 0
while i < a:
    z = []
    w, s = map(int, input().split())
    q = pow(w - x, 2) + pow(s - y, 2)
    e = q ** 0.5
    z.append(e)
    z.append(w)
    z.append(s)
    d.append(z)
    i = i + 1
d.sort()
for x in d:
    print(x[1], end=" ")
    print(x[2])