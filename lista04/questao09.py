while (True):
    opcao = int(input("Digite uma opcao (1 a 3)"))
    if(opcao == 1):
        num1 = int(input("Digite um numero"))
        num2 = int(input("Digite um numero"))
        print(f"A soma é igual a {num1+num2}")
    elif(opcao ==2 ):
        num1 = int(input("Digite um numero"))
        num2 = int(input("Digite um numero"))
        print(f"A subtracao é igual a {num1-num2}")
    elif(opcao == 3):
        
        break
    else:
        print("Opcao invalida")