#LISTA DORIVAL - GIT HUB
#EXERCICIO 10
def eh_kaprekar(k):
    k_quadrado = k ** 2
    num_digitos = len(str(k))
    parte_direita = k_quadrado % (10 ** num_digitos)
    parte_esquerda = k_quadrado // (10 ** num_digitos)
    return parte_esquerda + parte_direita == k

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))
for numero in range(inicio, fim + 1):
    if eh_kaprekar(numero):
        print(numero)
