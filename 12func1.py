def histogram(list):
    for i in range(len(list)):
        arr = [] 
        for j in range(list[i]):
            arr.append('*')
        print(*arr)

histogram(list = list(map(int, input().split())))
