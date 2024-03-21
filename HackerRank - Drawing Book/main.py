# Drawing Book
#Easy, Problem Solution

import math
import os
import random
import re
import sys

def pageCount(n, p):
    # Write your code here
    list_pages = []
    for i in range(n+1):
      list_pages.append(i)
  
    print(list_pages)
    front = p//2

    if(n%2 == 1):
      back = (n-p)//2
    else:
      back = (n-p+1)//2

    return(min(front, back))