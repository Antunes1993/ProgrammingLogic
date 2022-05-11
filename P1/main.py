# %%
s1 = "abcdabb"
s2 = "dcbabbb"

#First Option - Sort Function 
def are_anagrams(s1, s2):
    if((len(s1) != len(s2))):
        return False
    else: 
        return sorted(s1) == sorted(s2)

#print(are_anagrams(s1, s2))

#Second Option - Counter Function
from collections import Counter
from turtle import pen 

def are_anagrams(s1, s2):
    if(len(s1) != len(s2)):
        return False
    else:
        c1 = Counter(s1)
        c2 = Counter(s2)
        print(c1)
        return c1 == c2

print(are_anagrams(s1, s2))


# %%
#Third Option - Hash Table 
#Hash Table - A data structure that stores unique keys to values.  
def are_anagrams(s1, s2):
    if (len(s1) != len(s2)):
        return False

    freq1 = {}
    freq2 = {}

    #Frequency table for s1 
    for item in s1: 
        if item in freq1:
            freq1[item] += 1    
        else: 
            freq1[item] = 1

    for item in s2: 
        if item in freq2:
            freq2[item] += 1
        else:
            freq2[item] = 1

    print(freq1)
    return freq1 == freq2

print(are_anagrams(s1, s2))
# %%
