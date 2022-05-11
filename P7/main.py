# %%
import numpy as np 
nums = [1,4,5,6,7,3,2,15,8,9,14]
nums_sorted = np.sort(nums)
print (nums_sorted)
# %%
start = 0 
end = len(nums_sorted) - 1; 
target = 8 

cont = 0

# %%
def binary_search(nums, start, end, target, cont):
    mid_Index = round((start+end)/2)
    print("mid_index: ", mid_Index, " target:", target, "nums ind: ", nums[mid_Index])
    cont +=1
    #print (cont)
    if (nums[mid_Index] == target): 
        return True 
    elif (nums[mid_Index] > target): 
        return binary_search(nums, start, mid_Index-1, target, cont)
    elif (nums[mid_Index] < target): 
        return binary_search(nums, mid_Index+1, end, target, cont)
    

print(binary_search(nums_sorted, start, end, target, cont))
