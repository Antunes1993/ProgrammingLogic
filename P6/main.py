[Duvida]
def subarraysSum(nums, k):
    cnt = 0 
    soma = 0
    if k == 0: 
        return 0 
    else:
        for i in range(len(nums)):
            soma = (nums[i] + nums[i-1])
            print(i, " ", soma)
    return soma




nums = [1, 2, 3] 
k = 2
subarraysSum(nums, k)
# %%
