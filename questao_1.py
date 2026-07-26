def transforma_base (lista_dics):
    #Lista separada por níveis
    lista_niveis = {}

    for dic in lista_dics:
        nivel = dic['nivel'] #para pegar os values da key  'nivel'
        if nivel not in lista_niveis: # se não tiver sido adicionado na lista nova 
            lista_niveis[nivel] = [] #adiciona uma lista nova e vazia ao dic
        lista_niveis[nivel].append(dic) # senão: adiciona o dic todo
    return lista_niveis


