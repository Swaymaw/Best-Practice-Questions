def group_anagrams(strs):
    unique = [] 
    ans = []
    for i in range(len(strs)):
        v = sorted(strs[i])
        if v not in unique:
            unique.append(v)
            ans.append([])
        j = unique.index(v)
        ans[j].append(strs[i])
    
    return ans

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

