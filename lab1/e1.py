n, f = map(int, input().split())
sum = 0
for i in range(2 , n):
    if n % i != 0:
        sum += 1
if sum == n - 2 and n < 500 and f % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")


