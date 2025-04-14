#LISTA DORIVAL - GIT HUB
#EXERCICIO 5
numero = int(input("Digite um número: "))
while numero > 1:
    if numero % 1 == numero and numero % numero == 1:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
        break