#Para verificar se uma árvore é simétrica, o que precisamos fazer é verificar se as duas subárvores esquerda e direita são iguais.
#Devemos processar a raiz e chamar a função recursivamente para as subárvores esquerda e direita.

# Por exemplo, para obter a soma dos valores da árvore, fazemos: 

def tree_sum(root):
    if root is None:
        return 0
    else:
        left = tree_sum(root.left)
        right = tree_sum(root.right)
        return root.value + left + right

#Voltando ao exemplo:
def are_symetric(root1, root2):
    if root1 is None and root2 is None:
        return True 
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symetric(root1.left, root2.right) and are_symetric(root1.right, root2.left)


def is_symetric(root):
    if root is None:
        return True
    else:
        return are_symetric(root.left, root.right)

        

    
 
