all = int(input())
num = input().split()[:all]
list = []
for i in num:
    list.append(i)
list2 = []
list2.append(-1)
for j in range(1, all):
    ft = False
    for k in range(j-1, -1, -1):
        if list[j]>=list[k]:
            list2.append(list[k])
            ft = True
            break
    if ft == False:
        list2.append(-1)

print(*list2)


