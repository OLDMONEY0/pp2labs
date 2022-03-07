import re

x = input()

r = re.findall("[a-z]+_[a-z]+", x)
if r:
    print("Match")
else:
    print("No")