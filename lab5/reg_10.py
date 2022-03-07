import re
x = input()

r = re.sub(r"([a-z])([A-Z])", r"\1_\2", x).lower()
print(r)
