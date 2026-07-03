n = int(input("Digite um numero"))

print(f"Os multiplos de {n} de 1 ate 10 sao:")
for x in range(1, 11):
    print(f"{n*x}")
    