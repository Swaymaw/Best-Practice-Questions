def two_sum(nums, target):
    visited = {}

    for i, num in enumerate(nums):
        if target - num in visited.keys():
            return [i, visited[target-num]]
        else:
            visited[num] = i
