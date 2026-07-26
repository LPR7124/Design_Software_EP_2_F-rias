def valida_questao (questao):
    dic_final = {}
    
    #Verificar as condições inválidas (não encontradas)
    #Condição do titulo
    if 'titulo' not in questao:
        dic_final['titulo'] = 'nao_encontrado'
    else:
        if len(questao['titulo']) ==0 or questao['titulo'].strip() == '':
            dic_final['titulo']= 'vazio'

    # Condição do nível
    if 'nivel' not in questao:
        dic_final['nivel'] = 'nao_encontrado' 
    else:
        if questao['nivel'] != 'facil' and  questao['nivel'] != 'medio' and  questao['nivel'] != 'dificil':
            dic_final['nivel']= 'valor_errado'

    #Condição das opções
    if 'opcoes' not in questao:
        dic_final['opcoes'] = 'nao_encontrado'
    else:
        #Guardar o dicionário de opções da questão numa variável
        opcoes = questao['opcoes']
        if len(opcoes) != 4:
            dic_final['opcoes'] = 'tamanho_invalido'
        #Se existir, tiver o tamanho 4 mas não tiver notas (letras) válidas
        elif 'A' not in opcoes or 'B' not in opcoes or 'C' not in opcoes or 'D' not in opcoes:
            dic_final['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        #Se conseguiu passar por essas validações
        else:
            #Acessar o dicionário do valor de 'opcoes'
            for nota in opcoes:
                # Seguindo a mesma regra de tamanho ou vazio (strip() evita que seja inválido se só huver espaço no final)
                if len(opcoes[nota]) == 0 or opcoes[nota].strip() == '':
                    if 'opcoes' not in dic_final:
                        # Se opcoes ainda não existir, criar 
                        dic_final['opcoes'] = {}
                    # Se entrou no if --> vazio e existe:
                    dic_final['opcoes'][nota] = 'vazia'
                        

    #Validação do 'correta'
    if 'correta' not in questao:
        dic_final['correta'] = 'nao_encontrado' 
    
    else:
        # Se as notas não forem válidas
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            dic_final['correta'] = 'valor_errado'
    # Se o tamanho não foi compatível
    if len(questao) != 4:
        dic_final['outro'] = 'numero_chaves_invalido'

    return dic_final
    
