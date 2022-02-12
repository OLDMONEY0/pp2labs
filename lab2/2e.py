v = input().split()
if len(v) == 1:
    vt = input()
    v.append(vt)

v1 = int(v[0])
v2 = int(v[1])
arr = []
for i in range(v1):
    arr.append(v2 + 2*i)

x = arr[0]
for j in range(1,len(arr)):
    x = x ^ arr[j]

print(x)