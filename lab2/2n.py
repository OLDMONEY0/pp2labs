a = []
b = 1

while b != 0:
    b = int(input())
    if(b == 0):
        break
    a.append(b)

if(len(a) % 2 == 0):
    for i in range(len(a)):
        if i == len(a) // 2:
            break
        sum = a[i] + a[len(a) - 1 - i]
        print(sum, end=' ')
else:
    for i in range(len(a)):
        if i == len(a) // 2:
            print(a[i], end=' ')
            break
        sum = a[i] + a[len(a) -1 - i]
        print(sum, end=' ')