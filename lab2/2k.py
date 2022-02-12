soilem = input()

soilem = soilem.replace('!','').replace('?' , '').replace(',' , '').replace('.', '')

arr = []
for soz in soilem:
    if soz not in arr:
        arr.append(soz)

arr.sort
