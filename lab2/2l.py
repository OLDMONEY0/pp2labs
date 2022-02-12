a = input()
s = []
if len(a) % 2 == 1:
    print("No")
    exit()
for x in a:
    if x == "(" or x == "[" or x == "{":
        s.append(x)
    elif len(s) == 0 and x == ")":
        print("No")
        exit()
    elif len(s) == 0 and x == "]":
        print("No")
        exit()
    elif len(s) == 0 and x == "}":
        print("No")
        exit()
    elif s[-1] == "(" and x == ")":
        s.pop()
    elif s[-1] == "[" and x == "]":
        s.pop()
    elif s[-1] == "{" and x == "}":
        s.pop()
    else:
        break
if len(s) == 0:
    print("Yes")
else:
    print("No")