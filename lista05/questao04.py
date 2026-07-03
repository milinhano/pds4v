soma = 0
for x in range(5):
    v = int(input("Digite um numero: "))
    soma = soma + v

    if x == 0: #Primeira iteração
        maior = menor = v
    else: #Verificar o menor e o maior
        if(v > maior):
            maior = v
        if(v < menor):
            menor = v

media = soma/5
print(f"A media é igual a {media}")
print(f"O maior numero digitado foi {maior}")
print(f"O menor numero digitado foi {menor}")
