def three_sum(nums):
    # solution from leetcode: (Optimized)
    n = len(nums)
    ans = set()
    nums = sorted(nums)

    for i in range(n):
        j = i+1
        k = n-1
        while j <= k:
            s = nums[i] + nums[j] + nums[k]
            if i != j and i != k and j != k and  s == 0:
                ans.add((nums[i],nums[j],nums[k]))
                j += 1
                k -= 1
            elif s>0:
                k -= 1
            else:
                j += 1
    return ans
# Gives TLE- Error
#     ans = []
#     tmp = []

#     for i in range(len(nums)-1):
#         for j in range(i + 1, len(nums)):
#             check = -(nums[i] + nums[j])
#             if check in tmp:
#                 val = sorted([nums[i], nums[j], check])
#                 if val not  in ans:
#                     ans.append(val)
#         tmp.append(nums[i])
    
#     return ans 

# print(three_sum([-1,0,1,2,-1,-4]))
