#Migratory Birds
#Easy - Problem solving (basic)

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
  bird_ids = list(set(arr))
  count_birds = {}
  
  for item in bird_ids:
    count_birds[item]= arr.count(item)

  max_count = max(count_birds.values())
  max_count_birds = {bird_id: count for bird_id, count in count_birds.items() if count == max_count}
  
  return (min(max_count_birds.keys()))

arr = [1,1,2,2,3]
migratoryBirds(arr)