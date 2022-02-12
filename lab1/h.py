a = input()
b = input()
x = a.find(b)

for i in range(x, len(a)):
    if a[i] == b:
        y = i
if x != y:
    print(x, y)
else:
    print(x)
    

    