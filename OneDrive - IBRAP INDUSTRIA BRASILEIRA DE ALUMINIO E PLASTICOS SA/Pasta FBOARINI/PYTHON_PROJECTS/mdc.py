#MDC

a = 420
b = 66
c = 0

def mdc(a,b):

    while b > 0:
        c = a / b
        b = a % b
        a = int(c)
    mdc(a,b)

print(b)