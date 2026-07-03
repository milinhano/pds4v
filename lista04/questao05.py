soma = 0
while True:
    n = int(input("Digite um numero (zero para finalizar): "))
    if(n == 0):
        break
    soma = soma + n

print (f"{soma}")