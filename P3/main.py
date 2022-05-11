# %%
#First option
def kth_largest(arr, k):
    for i in range (k):
        arr.remove(max(arr))
    return max(arr)
arr = [1,2,5,5,9,8,6,7]
k = 3
print(kth_largest(arr, k))

# %%
#Second option
def kth_largest(arr, k):
    arr.sort()        
    return arr[-k]

arr = [1,2,5,5,9,8,6,7]
k = 1
print(kth_largest(arr, k))
