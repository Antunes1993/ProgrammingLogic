import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    results = []
    ranked_list = list(set(ranked))
    #ranked_list = sorted(ranked_list, reverse=True)
    ranked_list.sort()
    i=0
    for score in player:
      #i=0
      
      while (i<len(ranked_list) and score >= ranked_list[i]):        
          
        i+=1

      results.append(len(ranked_list) - i+1)
    return results