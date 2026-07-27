#Primeiras perguntas do jogo

print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!   ")  # Saudação inicial
jogador = input("Qual seu nome? ")  # Pede o nome do jogador

print(f'Ok {jogador.upper()}, você tem direito a pular 3 vezes e 2 ajudas! ')  # Informa pulos e ajudas disponíveis
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')  # Mostra as opções válidas

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
    for i, erro in enumerate(validacoes, start=1):
        if erro:
            print(f'Questão {i}: {erro}')
    continuar = 'exit'
else:
    #Filtra por nível (dicionário)
    questoes_niveis = transforma_base(lista_questoes)  

#ganhos disponíveis caso a resposta esteja certa 
premios = [1000.00, 5000.00, 10000.00, 30000.00, 50000.00, 100000.00, 300000.00, 500000.00, 1000000.00]
# Índice atual na lista de prêmios
indice_premio = -1  
# Valor atual do prêmio do jogador
premio_inicial = 0.00
# Total de pulos disponíveis
pulos = 3  
# Total de ajudas disponíveis
ajudas = 2
# Controle do loop principal
continuar = '' 
# Lista de questões já sorteadas
lista_questoes_sorteadas = []  

# Variáveis de progressão de nível (inicialmente no nível 'facil')
niveis = ['facil', 'medio', 'dificil']
indice_atual = 0
nivel_atual = niveis[indice_atual]
contou_certo = 0


# Loop principal do jogo
while continuar != 'exit':  

    #Filtranndo as perguntas com as funções anteriores (usa nível atual)
    questao_inedita = sorteia_questao_inedita(questoes_niveis, nivel_atual, lista_questoes_sorteadas)
    lista_questoes_sorteadas.append(questao_inedita)  
     # Exibe a questão em formato de texto
    print(questao_para_texto(questao_inedita, 1)) 

    # Controla para ver se o jogador quer continuar ou sair do jogo
    pergunta_atual = True  
    # Controla uso de ajuda na pergunta atual
    ajuda_usada = False 
    #Se continua a responder e não digitou exit, entra no loop de respostas
    
    while continuar != 'exit' and pergunta_atual:  
        # Lê a resposta do jogador
        resposta = input("Qual sua resposta?! ").strip().lower()  

        # Se digitou 'exit' ou 'parar' para encerrar 
        if resposta == 'exit' or resposta == 'parar':  
            continuar = 'exit'  
            pergunta_atual = False

        # Se o jogador quiser pular
        elif resposta == 'pula':  
            # Verifica se ainda há pulos para o jogador usar 
            if pulos > 0: 
                # diminui a quantidade de pulos disponíveis 
                pulos -= 1  
                # Informa quantos pulos restam
                print(f'Ok, pulando! Você ainda tem {pulos} pulos!')  
                # Pausa antes de seguir
                input('Aperte ENTER para continuar... ')  
                # Encerra a pergunta para sortear outra
                pergunta_atual = False  
            else:
                # Mensagem impressa caso não haja mais pulos 
                print('Você não tem mais pulos!')  

        elif resposta == 'ajuda':
            # Se o jogador pedir ajuda
            if ajuda_usada:
                print('Você já usou ajuda nesta pergunta!')
            elif ajudas > 0:
                # diminui a quantidade de ajudas disponíveis
                ajudas -= 1
                ajuda_usada = True
                # Exibe as opções erradas que podem ser descartadas
                print(gera_ajuda(questao_inedita))
                print(f'Você ainda tem {ajudas} ajudas!')
                input('Aperte ENTER para continuar... ')
            else:
                # Mensagem caso não haja mais ajudas
                print('Você não tem mais ajudas!')

        # Se a resposta estiver correta
        elif resposta == questao_inedita['correta'].lower():
            # Atualiza índice de prêmio se houver próximo valor
            if indice_premio < len(premios) - 1:
                indice_premio += 1
            # Atualiza o valor do prêmio atual
            premio_inicial = premios[indice_premio]
            # Conta acerto para progressão de nível
            contou_certo += 1
            print(f'Você acertou! Seu prêmio atual é de R$ {premio_inicial:.2f}')

            # Verifica se deve promover de nível (a cada 3 acertos)
            if contou_certo >= 3:
                if indice_atual < len(niveis) - 1:
                    indice_atual += 1
                    nivel_atual = niveis[indice_atual]
                    contou_certo = 0
                    print(f'Parabéns! Você avançou para o nível {nivel_atual.upper()}!')
                else:
                    # Já no nível máximo
                    contou_certo = 0

            # Caso o jogador tenha zerado o jogo (ganhou o prêmio máximo)
            if premio_inicial == 1000000.00:
                print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
                # Encerra o jogo após zerar
                continuar = 'exit'
            else:
                continuar = input('Aperte ENTER para continuar ou digite parar para sair: ').strip().lower() 
            # Encerra a pergunta atual 
            pergunta_atual = False  

        elif resposta in ['a', 'b', 'c', 'd']:
            # Resposta inválida para a questão atual
            print('Que pena! Você errou e vai sair sem nada :(')  
            continuar = 'exit' 
            pergunta_atual = False  

        else:
            # Opção inválida, permite tentar de novo
            print('Opção inválida. Use A, B, C, D, pula, ajuda ou parar.')

 # Mensagem final
if continuar == 'exit':  
    print('Jogo encerrado. Obrigado por jogar!')


