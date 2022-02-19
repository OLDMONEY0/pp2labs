a = list(map(int, input().split()))
arr = list(filter(lambda x: x % 2 != 0, a))
print(arr)
