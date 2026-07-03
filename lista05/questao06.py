consumoTotal = 0
produto = 0
maiorMateriaPrima = 0

for x in range(1,8):
    print(f"Materia prima 0{x}")
    ct = int(input("Consumo: "))
    consumoTotal = consumoTotal + ct
    if x == 1:
        maiorMateriaPrima = ct
        produto = x
    else:
        if (ct > maiorMateriaPrima):
            maiorMateriaPrima = ct
            produto = x

print(f"Consumo total: {consumoTotal}")
print(f"O produto 0{produto} consumiu {maiorMateriaPrima}kg")



#lista =[]
#for x in range(1,8):
#    print(f"Produto 0{x} ")
#    n = int(input("Quantide de materia prima: "))
#    lista.append(n) 

#print(lista)
