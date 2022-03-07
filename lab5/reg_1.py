import re


x = input()
r = re.findall("ab*", x)

if r:
    print("Match")
else:
    print("No")