b = int(input())
t = str(input())

if t == 'k':
    a = input()
    c = "{:." + a + "f}"
    print(c.format(b / 1024 ))
else:
    print(b * 1024)
