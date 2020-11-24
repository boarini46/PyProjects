

v = [44,23,21,55,66,89,74,32,78,90,98,79,112,250,554,344,321,114,167,1,5,7,9]



def busca(n):
    if n in v:
        v.sort()
        R = v.index(n)
        return R
    else:
        return "none"
    

ent = int(input("Digite o valor procurado: "))

res = busca(ent)

if res == "none":
    print('O valor procurado não está no vetor "v"')
else:
    print('O valor procurado está na posição: '+str(res)+' do vetor "v" agora ordenado')
