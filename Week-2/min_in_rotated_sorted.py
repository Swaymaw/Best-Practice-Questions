def findMin(nums):
    l = 0 
    r = len(nums) - 1
    ans = nums[0]

    while r > l:
        mid = (l + r) // 2
        if nums[mid] >= nums[r]:
            l = mid + 1   
        else:
            r = mid 

        ans = min(ans, nums[l])
    
    return ans

print(findMin([2, 1])) 



