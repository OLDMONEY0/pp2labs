n = int(input())
arr = []
a = map(int, input().split())
for x in a:
    arr.append(x)
arr.sort(reverse=True)
print(arr[0] * arr[1])