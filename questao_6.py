from questao_1 import *
from questao_2 import *
from questao_3 import *
from questao_4 import *
from questao_5 import *

def questao_para_texto (questao, id):
    linhas = f'----------------------------------------\n'
    primeira = f"QUESTAO {id}\n"
    segunda = f'\n'
    terceira = f'{questao["titulo"]}\n'
    quarta = f'\n'
    quinta = f'RESPOSTAS:\n'
    sexta = f'A: {questao["opcoes"]["A"]}\n'
    setima = f'B: {questao["opcoes"]["B"]}\n'
    oitava = f'C: {questao["opcoes"]["C"]}\n'   
    nona = f'D: {questao["opcoes"]["D"]}\n'
    

    return linhas + primeira + segunda + terceira + quarta + quinta + sexta + setima + oitava + nona 