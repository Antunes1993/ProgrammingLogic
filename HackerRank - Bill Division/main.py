#Bill Division
#Easy - Problem solving (basic)

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
  total_bill_each = sum(bill)/2
  correct_bill_anna = total_bill_each - (bill[k]/2)
  
  if (b==correct_bill_anna):
    print("Bon Appetit")
  else:
    print(int(total_bill_each - correct_bill_anna))

bill = [3,10,2,9]
k=1
b = 12
bonAppetit(bill, k, b)