def pr_Num(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    else:
        return True
nums = list(map(int, input().split()))
max = max(nums)
for i in nums:
    nums = filter(lambda x: pr_Num(x) == True, nums)
print(*nums)