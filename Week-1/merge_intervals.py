def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    i = 0
    while i < len(intervals)-1:
        x1 = intervals[i]
        x2 = intervals[i+1]
        if x1[1] >= x2[0]:
            intervals.remove(x1)
            intervals.remove(x2)
            intervals.insert(i, [x1[0], max(x1[1], x2[1])]) 
        else:
            i += 1
    
    return intervals


print(merge([[1,4],[4,5]]))