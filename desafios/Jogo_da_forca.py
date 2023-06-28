import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
response = requests.get(url)
palavras = response.text.split('\n') #ARMAZENA AS PALAVRAS EM UMA LISTA COM QUEBRA DE LINHA
secreta = random.choice(palavras).upper()

secreta = secreta.upper() #transforma a palavra e MAIUSCULA
palavra = '*' * len(secreta) #CRIA UMA STRING COM * COM O TAMANHO DA PALAVRA
vidas = 10 #QUANTIDADE DE VIDAS
digitadas = '' #ARMAZENA LETRAS DIGITADAS
print(palavra) #PRINTA A PALAVRA COM *

def limpar_tela():         # LIMPA A TELA
    if os.name == 'nt':
        os.system('cls')   #SE FOR Windows
    else:
        os.system('clear') #SE FOR LINUX E MacOS

while vidas > 0: # repetição enquanto a vida for >0
    letra = input('Digite uma letra: ').upper() # solicitação para digitar uma letra

    if digitadas.find(letra) >= 0: #verifica se a letra ja foi digitada
        print('Essa letra já foi digitada. Tente novamente.')
        continue
    else:
        digitadas += letra # se ainda não foi digitada a letra é armazenada em (Digitadas)

    if letra not in secreta: # se a letra não estiver na palavra secreta
        vidas -= 1 # é retirada uma vida
        print(f'A letra "{letra}" não está na palavra secreta. Você perdeu uma vida. Vidas restantes: {vidas}')

    auxiliar = list(palavra) #lista criada para atualiozar as letras adivinhadas
    for i in range(len(secreta)): #percorre cada posição da palavra secreta verificando se a letra é igual ´e igual a posição 'i'
        if letra == secreta[i]:
            auxiliar[i] = letra

    palavra = ''.join(auxiliar) #join junta todos os elemntos da lista auxiliar em uma string 
    limpar_tela() #limpoa a tela
    print(palavra) #printa a palavras com as letras descobertas
    print(f'Você ainda tem {vidas} vidas')

    if '*' not in palavra: #verifica se ainda não falta letra
        print('Parabéns! Você acertou a palavra secreta.')
        break

if vidas == 0: #se vida <0, perde o jogo
    print(f'Você perdeu! A palavra secreta era: {secreta}') 
