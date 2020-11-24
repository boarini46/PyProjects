class Fila_1(): # Fila Normal pessoas < 60 anos
    
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)
    
    def remover(self, x):
        if len(self.data) > 0:
            return self.data.pop(0) # remove o primeiro elemento da fila
    
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
    
    def empty(self):
        return not len(self.data) > 0 # retorna .T. caso a fila esteja vazia

#*****************************************************************************

class Fila_2(): # Fila prioritaria pessoas >= 60 anos
    
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)
    
    def remover(self, x):
        if len(self.data) > 0:
            return self.data.pop(0) # remove o primeiro elemento da fila
    
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
    
    def empty(self):
        return not len(self.data) > 0 # retorna .T. caso a fila esteja vazia        

#****************************************************************************

f1 = Fila_1()
f2 = Fila_2()
i = int(1)

for i in range(5): 

    idade = int(input('Digite a idade do cliente a entrar na fila: '))

    if idade < 60:
        f1.inserir(idade)
    else:
        f2.inserir(idade)

    print('Idade dos clientes atendimento normal: ' + str(f1.data))
    print('Idade dos clientes atendimento prioritario: ' + str(f2.data))

