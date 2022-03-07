import re
x = input()
r = re.sub('_','',x).title()
s = r.replace(" ","")
print(s)




