def unique_list(list):
    newlist = []
    for num in list:
        if num not in newlist:
            newlist.append(num)
    print(newlist)

unique_list(list = list(map(int, input().split())))