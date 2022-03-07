import re

x = input()

r = re.sub("[ , .]",":", x)

print(r)