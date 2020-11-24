
# Função de Leitura de Arquivos
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content) # retorna a quantidade de palavras e a quantidade de caracteres


#**************************************************************************************************************************

# Função de Recursão / Recursividade
def imprime_rec(l,i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l,i+1)

def fatorial(n):
    if n in [0, 1]: 
        return n
    else: 
        return n * fatorial(n-1)

#***************************************************************************************************************************
# Função de Memoização

m = dict()
def fat(n):
    if n == 0:
        return 1
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = n * fat(n-1)
        return m[n]


# Exemplo: n-ésimo termo da sequência de Fibonacci:
m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
    return m[n]

#***************************************************************************************************************************

m = dict()
def exercicio_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        m[n] = exercicio_1(n-1) + exercicio_1(n-2)
        m[n] = n-1
        return m[n]
    else:
        return m[n]
    

#***************************************************************************************************************************

print(exercicio_1(30))



#outfile = open('teste.txt', 'w')

#outfile.write('Olá classe!\n')

#idade = 30
#outfile.write('Sua idade é '+str(idade)+' anos.\n')
#outfile.write('Sua idade é {} anos.\n'.format(idade))


#n_words, n_chars = readFile('teste.txt')    
#print('O texto tem '+str(n_words)+' palavras e '+str(n_chars)+' caracteres')

#l = [1,2,3]
#imprime_rec(l)