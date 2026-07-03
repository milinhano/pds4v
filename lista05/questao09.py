#for aninhado
n= int(input("Digite um numero: "))

for x in range(n, 0,-1):
    for z in range (x):
        print("*", end =" ")
    print()
    