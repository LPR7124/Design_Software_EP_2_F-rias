from banco_de_perguntas import quest as lista_questoes
from questao_1 import transforma_base
from questao_5 import sorteia_questao_inedita

# Simulação da lógica de progressão (sem entrada do usuário)

questoes_niveis = transforma_base(lista_questoes)

premios = [1000.00, 5000.00, 10000.00, 30000.00, 50000.00, 100000.00, 300000.00, 500000.00, 1000000.00]
indice_premio = -1

niveis = ['facil', 'medio', 'dificil']
indice_atual = 0
nivel_atual = niveis[indice_atual]
contou_certo = 0

lista_questoes_sorteadas = []

print('Iniciando simulação de progresso de nível...')
print('Nível inicial:', nivel_atual)

# Simular 7 acertos alternando draws
for i in range(7):
    q = sorteia_questao_inedita(questoes_niveis, nivel_atual, lista_questoes_sorteadas)
    lista_questoes_sorteadas.append(q)
    # marca como acerto
    if indice_premio < len(premios) - 1:
        indice_premio += 1
    premio_atual = premios[indice_premio]
    contou_certo += 1
    print(f'Acerto {i+1}: prêmio agora R$ {premio_atual:.2f} (acertos no nível atual: {contou_certo})')
    if contou_certo >= 3:
        if indice_atual < len(niveis) - 1:
            indice_atual += 1
            nivel_atual = niveis[indice_atual]
            contou_certo = 0
            print(f'--> Promoção para nível {nivel_atual.upper()}!')
        else:
            contou_certo = 0

print('Simulação finalizada. Nível atual:', nivel_atual)
print('Prêmio atual:', premio_atual)
