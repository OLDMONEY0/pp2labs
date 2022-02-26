def sqr(N):
    for i in range(N):
        yield i ** 2

N = int(input())
a = sqr(N)
for i in a:
    print(i)
