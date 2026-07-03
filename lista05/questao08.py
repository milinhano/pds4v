n = input("Digite um numero")
d = input("Digite um digito(0 a 9): ")
contador = 0

for x in n:
    if x == d:
        contador = contador +1

print(f"O digito {d} aparece {contador} vezes no numero {n}")

