import random

def gera_ajuda(questao):
    opcoes = questao['opcoes']
    correta = questao['correta']

    # Monta a lista só com as respostas incorretas (sem a letra 'correta')
    incorretas = []
    for letra in opcoes:
        if letra != correta:
            incorretas.append(opcoes[letra])

    # Sorteia se vai mostrar 1 ou 2 dicas
    quantidade = random.randint(1, 2)

    # Sorteia índices sem repetir, até ter a quantidade desejada
    escolhidas = []
    indices_usados = []
    while len(escolhidas) < quantidade:
        indice = random.randint(0, len(incorretas) - 1)
        if indice not in indices_usados:
            indices_usados.append(indice)
            escolhidas.append(incorretas[indice])

    # Junta as opções escolhidas separadas por ' | '
    texto_opcoes = ' | '.join(escolhidas)

    dica = 'DICA:\nOpções certamente erradas: ' + texto_opcoes
    return dica

