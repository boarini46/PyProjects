import timeit

#x = 4
s = (int(input('Digite o Fibonacci: ')))



def fat(n): # FATORIAL
    if n == 0:
        return 1
    else:
        res = n * fat(n-1)
        return res



def fibonacci(s): # FIBONACCI
    if s <= 2:
        return 1
    else:
        f = fibonacci(s-2) + fibonacci(s-1)
        return f






#t = timeit.timeit() # Conta o Tempo - contagem inicial
#h = fat(x)
y = fibonacci(s)

#print("O fatorial de " + str(x) + " e: " + str(h))

print("Fibonacci de " + str(s) + " é: " + str(y))

#t1 = t - timeit.timeit() # Conta o Tempo - contagem final
#print("Tempo decorrido: " + str(t1))

