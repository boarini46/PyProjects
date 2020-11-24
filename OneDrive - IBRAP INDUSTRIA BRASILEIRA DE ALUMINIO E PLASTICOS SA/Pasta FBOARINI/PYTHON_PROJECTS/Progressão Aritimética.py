# Fórmula:
# Tn+1 = Tn+6
#T1 = 4
'''
n = int(input('Digite o termo da progressão aritimética: '))
L = []
S = 1
R = 1

def Tn(n):
    S = n + 6
    if R < n + 1:
        S = Tn(n + 6)
        R = R + 1
        L.append(S)
    return S


Tn(n)    


print('A progressão aritimética de ' + str(n) + ' é: ' + str(L))
'''

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
L = []

for c in range(primeiro,decimo + razao, razao):
    L.append(c)
    print(L) #print('{}'.format(c),end='-> ')
print('Fim...')
