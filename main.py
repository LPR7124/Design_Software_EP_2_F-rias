#Primeiras perguntas do jogo

print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!   ")
jogador = input("Qual seu nome? ")

print(f'Ok {jogador.upper()}, você tem direito a pular 3 vezes e 2 ajudas! ')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')

input('Aperte ENTER para continuar...')
print('O jogo já vai começar! Lá vem a primeira questão!')

print('Vamos começar com questões do nível FACIL! \n Aperte ENTER para continuar... ')

#importações
import banco_de_perguntas
from questao_1 import *
from questao_2 import *
from questao_3 import *
from questao_4 import *
from questao_5 import *
from questao_6 import *
from questao_7 import *

#Pega o banco de questões bruto (lista) e transforma em um dicionário que divide questões por nível
lista_questoes = banco_de_perguntas

#Filtra por nível (dicionário)
questoes_niveis = transforma_base(lista_questoes)

#premios disponíveis caso a resposta esteja certa 
premios = [1000.00, 5000.00, 10000.00, 30000.00, 50000.00, 100000.00, 300000.00, 500000.00, 1000000.00]
indice_premio = 0
continuar = ''

while continuar != 'exit':

    #Filtranndo as perguntas com as funções anteriores
    questao_sorteada = sorteia_questao(questoes_niveis, 'facil')
    lista_questoes_sorteadas = [questao_sorteada]
    questao_inedita = sorteia_questao_inedita(questoes_niveis, 'facil', lista_questoes_sorteadas)

    print(questao_para_texto(questao_inedita, 1))

    #Analizando a resposta do jogador
    resposta = input("Qual sua resposta?! ").strip().lower()
    if resposta == 'exit':
        continuar = 'exit'
    elif resposta == questao_inedita['correta'].lower():

        #Se a resposta estiver correta, o jogador recebe mais dinheiro e pode continuar
        if indice_premio < len(premios) - 1:
            indice_premio += 1
        premio_inicial = premios[indice_premio]
        print(f'Você acertou! Seu prêmio atual é de R$ {premio_inicial:.2f}')


        #Se o jogador acertar todas as questões, ele ganha o maior prêmio e o jogo termina
        if premio_inicial == 1000000.00:
            print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
            continuar = 'exit'
        else:
            continuar = input('Aperte ENTER para continuar ').strip().lower()
            
    else:
        print('Que pena! Você errou e vai sair sem nada :(')
        continuar = 'exit'

if continuar == 'exit':
    print('Jogo encerrado. Obrigado por jogar!')


