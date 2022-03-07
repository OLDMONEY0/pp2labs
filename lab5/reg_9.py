import re

x = input()

r = re.sub(r"([a-z])([A-Z])", r"\1 \2", x)
print(r)