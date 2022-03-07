import re

x = input()

r = re.findall("^a.*b$", x)
if r:
    print("Match")
else:
    print("No")