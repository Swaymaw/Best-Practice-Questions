def maxArea(height):
    l = 0 
    r = len(height) - 1
    ans = 0

    while r > l:
        ans = max(min(height[r], height[l])*(r-l), ans)

        if height[r] < height[l]:
            r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            r -= 1
            l += 1
        
    return ans

print(maxArea([1,8,6,2,5,4,8,3,7]))
