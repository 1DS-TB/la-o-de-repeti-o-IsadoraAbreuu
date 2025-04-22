#LISTA DORIVAL - GIT HUB
#EXERCICIO 6
numero = int(input("Digite o número de termos que deseja para a sequência de Fibonacci: "))
a, b = 0, 1
for i in range(numero):
    print(a, end=" ")
    a, b = b, a + b
