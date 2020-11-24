
ret = int
n = int

def S(n): # Recorrência
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        ret = 2 * S(n-1)
    return ret


n = int(input('Digite o valor para s: '))

print('O valor de retorno da recorrencia é: ' + str(S(n)))


