def containDuplicate(nums):
    nd_nums = set(nums)

    if len(nd_nums) == len(nums):
        return False 
    else:
        return True

print(containDuplicate([1, 2, 3 ,2]))
    

