def pal(s):
    ch = []
    s1 = []
    for i in s:
        ch.append(i)
        s1.append(i)
    ch.reverse()
    if ch == s1:
        print("True")
    else:
        print("False")

pal(s = input())
