import re

x = input()
r = re.findall("ab{2,5}", x)

if r:
    print("Match")
else:
    print("No")