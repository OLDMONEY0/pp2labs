import re

x = input()

r = re.findall("[A-Z]+[a-z]+", x)
if r:
    print("Match")
else:
    print("No")