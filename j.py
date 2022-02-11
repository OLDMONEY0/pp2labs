a = str(input())
b = a.split()
c = len(b)
for i in range(c):
    sum = 0
    l = b[i]
    for x in l:
        sum += 1
    if sum >= 3:
        print(l, end=" ")