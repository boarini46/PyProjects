
#Livro Fundamentos Matematicos para Computacao

# Tecnicas de Demonstracao = secao 2.1

#Para um inteiro positivo n, n fatorial é definido como n(n – 1)(n – 2) . . . 1, 
# e denotado por n!. Prove ou encontre um contraexemplo para a conjectura
# “Para todo inteiro positivo n, n! ≤ n2.”

x = 2 # x = valor para testar

def fat(n):
    if n == 0:
        return 1
    else:
        res = n * fat(n-1)
        return res


K = fat(x)  #(x-1)^2  # formula utilizada para K
L = x**2    #fat(x)/x # formula utilizada para L

if K <= L:
    print(str(K) + ' eh menor ou igual a ' + str(L))
else:
    print(str(K) + ' eh maior ou igual que ' + str(L))