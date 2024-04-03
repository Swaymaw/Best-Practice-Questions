def max_subarray(nums):
    max_sum = min(nums)
    l = 0 
    r = 1
    summ = 0
    while r <= len(nums):
        summ += nums[r-1]
        max_sum = max(summ, max_sum)
        if summ < 0:
            l = r 
            summ = 0 
        r += 1
    
    return max_sum 

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))