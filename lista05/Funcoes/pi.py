def pi():
    return 3.14

def areaCirculo(r):
    return pi() * r **2

raio = int(input("Digite o raio do cirulo: "))
areaC = areaCirculo(raio)
print(f"A area do circulo é igual a {areaC}")



