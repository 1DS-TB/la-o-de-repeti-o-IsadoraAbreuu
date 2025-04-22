#LISTA DORIVAL - GIT HUB
#EXERCICIO 5
numero = int(input("Digite um número para verificar se ele é primo: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo")
            break
    else:
        print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")
