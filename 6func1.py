def reverse_str(str):
    arr = []
    for i in range(len(str)):
        arr.append(str[len(str) - i - 1])
    print(*arr)

reverse_str(str = input().split())