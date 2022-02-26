def sqr(a,b):
    for i in range(a+1, b):
        yield i**2
a, b = int(input()), int(input())
for j in sqr(a,b):
    print(j)