x = int(input())
b = 0
arr =  [ [i+j for i in range(x)] for j in range(x) ]
for i in range(x):
    for j in range(x):
            if i == j:
                arr[i][j] = arr[i][0]*arr[0][j] 
            if i!=0 and  i < j:
                arr[i][j] = 0
            if j != 0 and i > j:
                arr[i][j] = 0
            print(arr[i][j], end=' ')
    print() 




        
            
