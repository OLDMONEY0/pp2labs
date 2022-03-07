import re
x = input()
r = re.split("(?=[A-Z])", x)
print(r)

