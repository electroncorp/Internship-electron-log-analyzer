def merge_and_sort(a, b):
    return sorted(a + b)

print(merge_and_sort([3,1,2], [5 ,4]))
print(merge_and_sort([], [3,2,1]))
print(merge_and_sort([-3,-1], [-2,0]))
print(merge_and_sort([1,1,2], [2,3]))
print(merge_and_sort([100], []))
