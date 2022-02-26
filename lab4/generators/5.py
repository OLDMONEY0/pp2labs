from re import I


def to_down(n):
    for i in range(n, 0, -1):
        yield i
a = to_down(n=int(input()))
for j in a:
    print(j)