#LISTA DORIVAL - GIT HUB
#EXERCICIO 11
import random
def duelo():
    while True:
        # jogador
        ataque_jogador = random.randint(1, 51)
        defesa_jogador = random.randint(1, 51)
        vida_jogador = random.randint(200, 1001)
        # inimigo
        vida_inimigo = vida_jogador
        ataque_inimigo = random.randint(1, 51)
        defesa_inimigo = random.randint(1, 51)

        print("************* DUELO ***************\n")
        print("------------- VOCÊ ----------------")
        print(f"             HP: {vida_jogador}\nATAQUE: {ataque_jogador}            DEFESA: {defesa_jogador}")
        print("------------ INIMIGO ---------------")
        print(f"             HP: {vida_inimigo}\nATAQUE: {ataque_inimigo}            DEFESA: {defesa_inimigo}\n")

        opcao = input("============= MENU ===============\n[1] Começar o jogo!\n[2] Sair do jogo!\nESCOLHA: ")

        if opcao == "1":
            print("\n!!!!!! START NO JOGO !!!!!!\n")
            turno = 1
            while vida_jogador > 0 and vida_inimigo > 0:
                print(f"------------ TURNO {turno} ---------------")
                print(f"SEU HP: {vida_jogador}      | HP INIMIGO: {vida_inimigo}")
                escolha = input("\n[1] Atacar OU [2] Curar ?\nESCOLHA: ")

                if escolha == "1":
                    dano_jogador = ataque_jogador - defesa_inimigo
                    if dano_jogador < 0:
                        dano_jogador = 0
                    vida_inimigo -= dano_jogador
                    print(f"Você atacou! Inimigo perdeu {dano_jogador} HP.")
                elif escolha == "2":
                    cura = 20
                    vida_jogador += cura
                    print(f"Você se curou! Você ganhou {cura} HP.")
                else:
                    print("ERRO - Opção inválida.")
                    break

                acao_inimigo = random.choice(["atacar", "curar"])
                if acao_inimigo == "atacar":
                    dano_inimigo = ataque_inimigo - defesa_jogador
                    if dano_inimigo < 0:
                        dano_inimigo = 0
                    vida_jogador -= dano_inimigo
                    print(f"O inimigo atacou! Você perdeu {dano_inimigo} HP.\n")
                elif acao_inimigo == "curar":
                    cura = 20
                    vida_inimigo += cura
                    print(f"O inimigo se curou! Ele ganhou {cura} HP.\n")
                else:
                    print("ERRO - Opção inválida.")
                    break

                turno += 1

            if vida_jogador <= 0 and vida_inimigo <= 0:
                print("EMPATE! OS DOIS CAÍRAM JUNTOS.\n")
                print("_______________________________________________")
            elif vida_jogador <= 0:
                print("VOCÊ PERDEU! FIM DE JOGO.\n")
                print("_______________________________________________")
            else:
                print("VOCÊ VENCEU, PARABÉNS! FIM DE JOGO.\n")
                print("_______________________________________________")

        if opcao == "2":
            print("\n!!!!!! VOCÊ SAIU DO JOGO !!!!!!\n")
            break

duelo()
