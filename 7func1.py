def has_33(nums):
    pass
    for i in range(len(nums)):
        if nums[i]==3:
            if nums[i+1]==3:
                return True
            else:
                return False
      

nums = list(map(int, input().split()))
print(has_33(nums))

