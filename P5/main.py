
from inspect import stack

def is_valid(stringParentheses):
    listParentheses = []
    for item in stringParentheses:
        if item == '(':
            listParentheses.append(item)
        else: 
            if len(listParentheses) == 0:
                return False
            else:
                listParentheses.pop()
    return len(listParentheses) == 0
print(is_valid('(()()()()())'))