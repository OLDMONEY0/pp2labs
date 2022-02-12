x = int(input())
arr =  [ ['#' for i in range(x)] for j in range(x) ]
for i in range(x):
    for j in range(x):
            if x % 2 == 0 and i < j:
                arr[i][j] = '.'
            if  x % 2 == 1 and  i < x - j - 1:
                arr[i][j] = '.'
            print(arr[i][j], end='')
    print() 