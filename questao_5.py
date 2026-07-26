from questao_1 import *
from questao_2 import *
from questao_3 import *
from questao_4 import *

def sorteia_questao_inedita (questoes_nivel, nivel, lista_questoes_sorteadas):
    # Pega no dicionário de questões um nivel já dado
    lista_nivel = questoes_nivel[nivel]

    #Uso a função randint para fazer o sorteio : sorteia um indice aleatório 
    indice_sorteado = random.randint(0, len(lista_nivel) - 1)

    #usa o índice aleatório sorteado 
    questao_sorteada = lista_nivel[indice_sorteado]

    # Verifica se a questão sorteada já foi sorteada antes
    while questao_sorteada in lista_questoes_sorteadas:
        indice_sorteado = random.randint(0, len(lista_nivel) - 1)
        questao_sorteada = lista_nivel[indice_sorteado]

    return questao_sorteada