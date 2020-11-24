a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

d = "String"

if a <= b and a <= c:
    if a <= c:
        print("Ordem Crescente: {},{},{}".format(a,b,c))
    else:
        print("Ordem Crescente: {},{},{}".format(a,c,b))
elif b <=a and b <= c:
    if a <= c:
        print("Ordem crescente: {},{},{}".format(b,a,c))
    else:
        print("Ordem crescente: {},{},{}".format(b,c,a))
else:
    if a <= b:
        print("Ordem crescente: {},{},{}".format(c,a,b))
    else:
        print("Ordem crescente: {},{},{}".format(c,b,a))


