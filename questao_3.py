from questao_1 import *
from questao_2 import *
def valida_questoes  (lista_questoes):
    lista_corrigida = []
    # Para cada questão da lista 

    for questao in lista_questoes:
        # é validada na função anterior
        dic_final = valida_questao(questao)
        #o dicionário é adicionado na lista_corrigida
        lista_corrigida.append(dic_final)
    return lista_corrigida

