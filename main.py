#Primeiras perguntas do jogo

print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!   ")  # Saudação inicial
jogador = input("Qual seu nome? ")  # Pede o nome do jogador

print(f'Ok {jogador.upper()}, você tem direito a pular 3 vezes e 2 ajudas! ')  # Informa pulos e ajudas disponíveis
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula", "parar" e "exit"!')  # Mostra as opções válidas

input('Aperte ENTER para continuar...')  # Aguarda ENTER para continuar
print('O jogo já vai começar! Lá vem a primeira questão!')  # Anúncio de início do jogo

print('Vamos começar com questões do nível FACIL! \n Aperte ENTER para continuar... ')  # Mensagem final antes do loop

 #importações
from banco_de_perguntas import quest as lista_questoes  # Importa a lista de perguntas do módulo
from questao_1 import *  
from questao_2 import *  
from questao_3 import *  
from questao_4 import *  
from questao_5 import *  
from questao_6 import *  
from questao_7 import *

 #Pega o banco de questões bruto (lista) e transforma em um dicionário que divide questões por nível
 # `lista_questoes` já importada acima a partir de banco_de_perguntas.quest

#Valida a base de perguntas antes de iniciar o jogo
validacoes = valida_questoes(lista_questoes)
if any(validacoes):
    print('Base de perguntas inválida. Verifique os erros abaixo:')
    i = 1
    for erro in validacoes:
        if erro:
            print(f'Questão {i}: {erro}')
        i += 1
    continuar = 'exit'
else:
    #Filtra por nível (dicionário)
    questoes_niveis = transforma_base(lista_questoes)  

#ganhos disponíveis caso a resposta esteja certa 
premios = [1000.00, 5000.00, 10000.00, 30000.00, 50000.00, 100000.00, 300000.00, 500000.00, 1000000.00]
# Controle do loop principal
continuar = '' 
# Lista de níveis disponíveis
niveis = ['facil', 'medio', 'dificil']

# Loop principal do jogo: só encerra quando o jogador digitar exit
while continuar != 'exit':
    # Estado inicial de cada partida
    indice_premio = -1
    premio_inicial = 0.00
    pulos = 3
    ajudas = 2
    lista_questoes_sorteadas = []
    indice_atual = 0
    nivel_atual = niveis[indice_atual]
    contou_certo = 0
    jogo_ativo = True

    numero_questao = 1
    while jogo_ativo and continuar != 'exit':
        # Filtranndo as perguntas com as funções anteriores (usa nível atual)
        questao_inedita = sorteia_questao_inedita(questoes_niveis, nivel_atual, lista_questoes_sorteadas)
        lista_questoes_sorteadas.append(questao_inedita)
        print(questao_para_texto(questao_inedita, numero_questao))

        pergunta_atual = True
        ajuda_usada = False

        while continuar != 'exit' and pergunta_atual:
            resposta = input("Qual sua resposta?! ").strip().lower()

            if resposta == 'exit':
                print(f'Ok! Você saiu e seu prêmio é de R$ {premio_inicial:.2f}')
                continuar = 'exit'
                pergunta_atual = False
                jogo_ativo = False

            elif resposta == 'parar':
                confirmacao = input(f'Deseja mesmo parar [S/N]? Caso responda "S", sairá com R$ {premio_inicial:.2f}! ').strip().lower()
                if confirmacao == 's':
                    print(f'Ok! Você parou e seu prêmio é de R$ {premio_inicial:.2f}')
                    continuar = 'exit'
                    pergunta_atual = False
                    jogo_ativo = False
                elif confirmacao == 'n':
                    print('Ok, continuando o jogo.')
                else:
                    print('Resposta inválida. Digite S ou N.')

            elif resposta == 'pula':
                if pulos > 0:
                    pulos -= 1
                    print(f'Ok, pulando! Você ainda tem {pulos} pulos!')
                    input('Aperte ENTER para continuar... ')
                    pergunta_atual = False
                else:
                    print('Você não tem mais pulos!')

            elif resposta == 'ajuda':
                if ajuda_usada:
                    print('Você já usou ajuda nesta pergunta!')
                elif ajudas > 0:
                    ajudas -= 1
                    ajuda_usada = True
                    print(gera_ajuda(questao_inedita))
                    print(f'Você ainda tem {ajudas} ajudas!')
                    input('Aperte ENTER para continuar... ')
                else:
                    print('Você não tem mais ajudas!')

            elif resposta == questao_inedita['correta'].lower():
                if indice_premio < len(premios) - 1:
                    indice_premio += 1
                premio_inicial = premios[indice_premio]
                contou_certo += 1
                print(f'Você acertou! Seu prêmio atual é de R$ {premio_inicial:.2f}')

                if contou_certo >= 3:
                    if indice_atual < len(niveis) - 1:
                        indice_atual += 1
                        nivel_atual = niveis[indice_atual]
                        contou_certo = 0
                        print(f'Parabéns! Você avançou para o nível {nivel_atual.upper()}!')
                    else:
                        contou_certo = 0

                if premio_inicial == 1000000.00:
                    print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
                    jogo_ativo = False
                else:
                    resposta_continuar = input('Aperte ENTER para continuar ou digite exit para sair: ').strip().lower()
                    if resposta_continuar == 'exit':
                        continuar = 'exit'
                        jogo_ativo = False
                pergunta_atual = False

            elif resposta in ['a', 'b', 'c', 'd']:
                print('Que pena! Você errou e vai sair sem nada :(')
                jogo_ativo = False
                pergunta_atual = False

            else:
                print('Opção inválida. Use A, B, C, D, pula, ajuda, parar ou exit.')

        if jogo_ativo and continuar != 'exit':
            numero_questao += 1

    if continuar != 'exit':
        reiniciar = input('Deseja jogar novamente? Aperte ENTER para começar outra partida ou digite exit para encerrar: ').strip().lower()
        if reiniciar == 'exit':
            continuar = 'exit'

if continuar == 'exit':
    print('Jogo encerrado. Obrigado por jogar!')


