total_horas = int(input("Digite a quantidade de horas: "))
hora = 1
total_pecas = 0

while (hora <= total_horas):
    print(f"Quantidade de pecas hora {hora}: ", end=" ")
    quant_pecas = int(input())
    total_pecas = total_pecas +quant_pecas
    hora = hora+1

print(f"Produção total = {total_pecas}")
print(f"MEdia da produçao = {total_pecas/total_horas}")