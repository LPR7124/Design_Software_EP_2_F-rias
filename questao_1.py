def transforma_base (lista_dics):
    #Lista separada por níveis
    lista_niveis = {}

    for dic in lista_dics:
        #para pegar os values da key  'nivel'
        nivel = dic['nivel'] 
        # se não tiver sido adicionado na lista nova 
        if nivel not in lista_niveis: 
            #adiciona uma lista nova e vazia ao dic
            lista_niveis[nivel] = [] 
        # senão: adiciona o dic todo
        lista_niveis[nivel].append(dic) 
    return lista_niveis


