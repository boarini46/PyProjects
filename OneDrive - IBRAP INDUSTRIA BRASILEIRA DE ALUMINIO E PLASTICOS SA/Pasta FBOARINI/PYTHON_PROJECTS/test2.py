x = int(1)
while x != 0:
    x = int(input("Digite o valor de x: "))
    if x % 2 == 0:
        print("%d é par " % x)
    else:
        print("%d é impar " % x)