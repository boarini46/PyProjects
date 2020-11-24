class Fila1(): # atendimento normal
    
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



class Fila2(): # atendimento prioritario
    
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





f1 = Fila1()
f2 = Fila2()

while True:

    a = int(input('Idade do cliente: '))

    if a > 59:
        f2.inserir(a)
        #f2.remover(a)
    else:
        f1.inserir(a)
        if len(f2.data) > 2:
            f1.remover(a)

    print(f1.data)
    print(f2.data)


