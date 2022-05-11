def validation_check(intPivo, intPreviousPivo, listParentheses, listParenthesesIndex, intNextPivo):
                 
                intPivo = intNextPivo
                listParentheses[listParenthesesIndex] += 1
                print(listParentheses, " ", intPivo)

                return intPivo, intPreviousPivo, listParentheses

def back_validation_check(intPivo, intPreviousPivo, listParentheses, listParenthesesIndex):
                intPivo = intPreviousPivo                
                listParentheses[listParenthesesIndex] -= 1
                print(listParentheses, " ", intPivo)
                return intPivo, intPreviousPivo, listParentheses



def isValid(s: str) -> bool:
    result = "String Valida"
    list_parentheses = [0,0,0]

    if len(s) == 0:
        result = "String vazia."
    
    else:
        pivo = ""
        previous_pivo = ""     
        for item in s:
            if item == '(':
                pivo, previous_pivo, list_parentheses = validation_check(pivo, previous_pivo, list_parentheses, 0, 1)

            elif item == '[':
                pivo, previous_pivo, list_parentheses = validation_check(pivo, previous_pivo, list_parentheses, 1, 2)    

            elif item == '{':
                pivo, previous_pivo, list_parentheses = validation_check(pivo, previous_pivo, list_parentheses, 2, 3)    
            
            
            elif item == ')':                
                if pivo != 1:
                    result = "String inválida1"
                else:
                    back_validation_check(pivo, previous_pivo, list_parentheses, 0)
            elif item == ']':                
                if pivo != 2:
                    result = "String inválida2"
                else:
                    back_validation_check(pivo, previous_pivo, list_parentheses, 1)
            elif item == '}':                
                if pivo != 3:
                    result = "String inválida3"
                else:
                    back_validation_check(pivo, previous_pivo, list_parentheses, 2)
            else: 
                s.pop() 
            


        for item in list_parentheses:
            if item != 0:
                result = "Não é um string válida."
        print (list_parentheses)
        return result 


result = isValid ("()[]{}")
print (result)
