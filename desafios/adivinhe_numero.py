import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100) #GERA UM NUMERO SECRETO
    numero_tentativas = 10 
    tentativas_feitas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while tentativas_feitas < numero_tentativas:
        tentativas_restantes = numero_tentativas - tentativas_feitas
        if tentativas_restantes <= 3:
            print(f"ATENÇÃO: Você tem apenas {tentativas_restantes} tentativas restantes!")

        palpite = int(input("Digite seu palpite: "))

        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        tentativas_feitas += 1

        if palpite < numero_secreto:
            print("O número correto é maior do que seu palpite.")
            print(f'Número de tentativas: {tentativas_feitas}')
        elif palpite > numero_secreto:
            print("O número correto é menor do que seu palpite.")
            print(f'Número de tentativas: {tentativas_feitas}')
        else:
            print("Parabéns! Você acertou o número!")
            print("Número de tentativas: ", tentativas_feitas)
            break
        print('_' * 70)

    if tentativas_feitas == numero_tentativas:
        print("Você esgotou o número de tentativas.")
        print("O número correto era:", numero_secreto)

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        adivinhe_o_numero()

adivinhe_o_numero()
