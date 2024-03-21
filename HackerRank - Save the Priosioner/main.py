#Save the prisioner
#Easy - Problem Solving
import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    # Write your code here
    res = s + m - 1

    if (res % n == 0):
      return n
    else:
      return res

prisioner=3
candy=7
initial_chair=3
saveThePrisoner(prisioner,candy,initial_chair)