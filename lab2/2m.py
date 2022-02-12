dts = []
while True:
    date = input()
    if date != '0':
        day = date[0:2]
        month = date[3:5]
        year = date[6:]
        dts.append(year + ' ' + month + ' ' + day)
    else:
        break
dts.sort()
for i in dts:
    year = i[0:4]
    month = i[4:8]
    day = i[8:10]
    print(day + month + year)