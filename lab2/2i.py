a = int(input())
i = 0
n = []
m = []
while i < a:
    s = input()
    x = s.split()
    if s[0] == "1":
        n.append(x[1])
    else:
        m.append(n[0])
        n.pop(0)
    i = i + 1
print(" ".join(m))