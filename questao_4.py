from questao_1 import *
from questao_2 import *
from questao_3 import *

import random
def sorteia_questao (questoes_nivel, nivel):
    # Pega no dic de questões um nivel dado
    lista_nivel = questoes_nivel[nivel]

    #Uso a função randint para fazer o sorteio : sorteia um indice aleatório 
    indice_sorteado = random.randint(0, len(lista_nivel) - 1)

    #usa o índice aleatório sorteado 
    questao_sorteada = lista_nivel[indice_sorteado]
    return questao_sorteada