def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        #
        linha = []
        for j in range(n_colunas):
            print(f"matriz[{i}][{j}] = ", end= " ")
            valor = int(input())
            linha += [valor]

        #
        matriz += [linha]
    
    return matriz

def imprimir_matriz(matriz, n_linhas, n_colunas):
    print(len(matriz))
    for i in range(n_linhas):
        for j in range(n_colunas):
            print(matriz[i][j], end= " ")
        print()
            
m = criar_matriz(2,3)
imprimir_matriz(m, 2, 3)

print(m)