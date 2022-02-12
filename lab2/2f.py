a = int(input())
b = {}
max = 0

for i in range(a):
    n, m = input().split()
    m = int(m)

    if b.get(n) == None:
        b[n] = m
    else:
        b[n] += m

    if max < b[n]:
        max = b[n]

for i, j in sorted(b.items()):
    if max - j == 0:
        print(i, 'is lucky!')
    else:
        print(i, 'has to receive', max - j, 'tenge')