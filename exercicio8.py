#LISTA DORIVAL - GIT HUB
#EXERCICIO 8
numero = int(input("Digite o número de termos para calcular a soma da série harmônica: "))
soma = 0
for i in range(1, numero + 1):
    soma += 1 / i
print(f"A soma da série harmônica até {numero} termos é: {soma:.2f}")
