def productExceptSelf(nums):
    n = len(nums)
    ans = [1]*n
    prodl = 1
    prodr = 1
    for i in range(n):
        # filling it with cumprod starting from left
        ans[i] *= prodl
        prodl *= nums[i]
        # filling this side with cumprod starting from right
        ans[n-i-1] *= prodr
        prodr *= nums[n-i-1]
    return ans 

print(productExceptSelf([1, 2, 3, 4]))