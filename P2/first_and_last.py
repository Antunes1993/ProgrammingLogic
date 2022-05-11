# %%
#First option 
def first_and_last(arr, target):
    contain_target = False
    for element in arr: 
        if element == target:
            start = list.index(element)  
            contain_target = True
            break 
    
    reversed_list = arr[::-1]
    for element in reversed_list:
        if element == target:
            end = len(reversed_list) - reversed_list.index(element) -1 
            contain_target = True 
            break
    if contain_target:
        return [start, end]
    else:
        return [-1, -1]


#Second option
def first_and_last(arr, target):
    contain_target = False
    for element in arr: 
        if element == target:
            start = list.index(element)              
            contain_target = True
            break 
    
    for i in range (len(arr)):
        if arr[i] == target:
            while i < len(arr):
                if arr[i+1] == target:
                    i += 1
                else:
                    end = i
                    contain_target = True
                    break
    
    if contain_target:
        return [start, end]
    else:
        return [-1, -1]

list = [1, 2, 3, 3, 3, 4, 5, 6]
target = 3 
first_and_last(list, target)
