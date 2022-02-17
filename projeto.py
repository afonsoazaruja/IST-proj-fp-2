"""
autor: Afonso Carraça Azaruja
email: afonso.azaruja@tecnico.ulisboa.pt / afonso.azaruja@gmail.com
data: 18/11/2021
"""

# AUXILIAR
def aux_tuplo_lista(t):
    lst = []
    for i in t:
        lst.append(i)
    return lst


def aux_lista_tuplo(lst):
    tp = ()
    for i in lst:
        tp += (i,)
    return tp


# TAD posicao --> R(x, y) = [x, y]
def cria_posicao(x, y):
    """ cria_posicao: int, int --> posicao
    Recebe dois inteiros positivos e devolve uma posição (x, y).
    """
    if not (type(x) == type(y) == int and x >= 0 and y >= 0):
        raise ValueError('cria_posicao: argumentos invalidos')
    return [x, y]


def cria_copia_posicao(p):
    """ cria_copia_posicao: posicao --> posicao
    Recebe uma posição e devolve uma cópia da posição
    """
    x, y = p[0], p[1]
    return [x, y]


def obter_pos_x(p):
    """ obter_pos_x: posicao --> int
    Recebe uma posição e devolve a componente x da posição
    """
    if eh_posicao(p):
        return p[0]


def obter_pos_y(p):
    """ obter_pos_y: posicao --> int
    Recebe uma posição e devolve a componente y da posição
    """
    if eh_posicao(p):
        return p[1]


def eh_posicao(p):
    """ eh_posicao: universal --> bool
    Recebe um argumento universal e devolve True se o argumento corresponder a uma posição, caso contrário False
    """
    if not (type(p) == list and len(p) == 2 and type(p[0]) == type(p[1]) == int and p[0] >= 0 and p[1] >= 0):
        return False
    return True


def posicoes_iguais(p1, p2):
    """ posicoes_iguais: posicao, posicao --> bool
    Recebe duas posições e devolve True caso sejam iguais, caso contrário, False
    """
    if eh_posicao(p1) and eh_posicao(p2):
        return obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)
    return False


def posicao_para_str(p):
    """ posicao_para_str: posicao --> str
    Recebe uma posição e devolve uma string da posição
    """
    return ('(' + str(obter_pos_x(p)) + ', ' + str(obter_pos_y(p)) + ')')


def obter_posicoes_adjacentes(p): # UTILIZA O CRIAR_POSICAO, QUE É ESTA MERDA????
    """ obter_posicoes_adjacentes: posicao --> tuple
    Recebe uma posição e devolve as posições adjacentes num tuplo, cima, direita, baixo e esquerda, nesta ordem
    """
    pos = ()
    if obter_pos_y(p) != 0:
        pos += (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1),)
    pos += (cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)),)
    pos += (cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1),)
    if obter_pos_x(p) != 0:
        pos += (cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p)),)
    return pos


def ordenar_posicoes(t):
    """ ordenar_posicoes: tuple --> tuple
    Recebe um tuplo com posições e devolve um tuplo com as posições ordenadas de acordo com a ordem de leitura do prado
    """
    return tuple(sorted(t, key = lambda x: (obter_pos_y(x), obter_pos_x(x))))


# TAD animal -->  R(s, r, a) = {'s' : s, 'r' : [idade, r], 'a' : [fome, a]}
def cria_animal(s, r, a):
    """ cria_animal: str, int, int --> animal
    Recebe uma cadeia de carateres, correspondendo à espécie do animal e dois valores inteiros correspondendo à
    frequência de reprodução e à frequência de alimentação do animal, devolvendo o animal
    """
    if not (type(s) == str and type(r) == type(a) == int and r > 0 and a >= 0) or s.isspace() or s == '':
        raise ValueError('cria_animal: argumentos invalidos')
    return {'s': s, 'r': [0, r], 'a': [0, a]}


def cria_copia_animal(ani):
    """ cria_copia_animal: animal --> animal
    Recebe um animal e devolve uma nova cópia do animal
    """
    s, r, a = ani['s'], ani['r'].copy(), ani['a'].copy()
    return {'s': s, 'r': r, 'a': a}


def obter_especie(ani):
    """ obter_especie: animal --> str
    Recebe um animal e devolve uma cadeia de carateres correspondendo à espécia do animal
    """
    return ani['s']


def obter_freq_reproducao(ani):
    """ obter_freq_reproducao: animal --> int
    Recebe um animal e devolve um inteiro correspondendo ao valor da frequência de reprodução do mesmo
    """
    return ani['r'][1]


def obter_freq_alimentacao(ani):
    """ obter_freq_alimentacao: animal --> int
    Recebe uma animal e devolve um inteiro correspondendo ao valor da frequência de alimentação do mesmo
    """
    return ani['a'][1]


def obter_idade(ani):
    """ obter_idade: animal --> int
    Recebe um animal e devolve um inteiro correspondendo ao valor da idade do mesmo
    """
    return ani['r'][0]


def obter_fome(ani):
    """ obter_fome: animal --> int
    Recebe um animal e devolve um inteiro correspondendo ao valor da fome do mesmo
    """
    return ani['a'][0]


def aumenta_idade(ani):
    """ aumenta_idade: animal --> animal
    Recebe um animal e devolve o mesmo com o valor da idade incrementado por 1
    """
    ani['r'][0] += 1
    return ani


def reset_idade(ani):
    """ reset_idade: animal --> animal
    Recebe um animal e devolve o mesmo com o valor da idade igual a 0
    """
    ani['r'][0] = 0
    return ani


def aumenta_fome(ani):
    """ aumenta_fome: animal --> animal
    Recebe um animal e devolve o mesmo com o valor da fome incrementado por 1
    """
    if obter_freq_alimentacao(ani) == 0:
        return ani
    else:
        ani['a'][0] += 1
        return ani


def reset_fome(ani):
    """ reset_fome: animal --> animal
    Recebe um animal e devolve o mesmo com o valor da fome igual a 0
    """
    if obter_freq_alimentacao(ani) == 0:
        return ani
    else:
        ani['a'][0] = 0
        return ani


def eh_animal(arg):
    """ eh_animal: universal --> bool
    Recebe um argumento, caso corresponda a um animal devolve True, caso contrário, False
    """
    if type(arg) != dict or len(arg) != 3 or 's' not in arg or 'r' not in arg or 'a' not in arg:
        return False
    if type(arg['s']) != str or type(arg['r']) != list or type(arg['a']) != list:
        return False
    if arg['s'].isspace() or arg['s'] == '' or len(arg['r']) != 2 or len(arg['a']) != 2:
        return False
    return obter_idade(arg) >= 0 and obter_freq_reproducao(arg) > 0 and obter_fome(arg) >= 0 and obter_freq_alimentacao(arg) >= 0


def eh_predador(ani):
    """ eh_predador: animal --> bool
    Recebe um animal, se este corresponder a um predador, devolve True, caso contrário, False
    """
    if eh_animal(ani):
        return obter_freq_alimentacao(ani) > 0
    return False


def eh_presa(ani):
    """ eh_presa: animal --> bool
    Recebe um animal, se este corresponder a uma presa, devolve True, caso contrário, False
    """
    if eh_animal(ani):
        return obter_freq_alimentacao(ani) == 0
    return False
    

def animais_iguais(ani1, ani2):
    """ animais_iguais: animal, animal --> bool
    Recebe dois animais e devolve True caso sejam iguais, caso contrário, False
    """
    if eh_animal(ani1) and eh_animal(ani2) and obter_especie(ani1) == obter_especie(ani2) and obter_idade(ani1) == obter_idade(ani2) and\
        obter_freq_reproducao(ani1) == obter_freq_reproducao(ani2) and obter_fome(ani1) == obter_fome(ani2) and obter_freq_alimentacao(ani1)\
            == obter_freq_alimentacao(ani2):
            return True
    return False


def animal_para_char(ani):
    """ animal_para_char: animal --> str
    Recebe um animal e devolve a cadeia de carateres correspondendo ao primeiro caráter da espécie do animal, maiúscula
    caso seja predador e minúscula para presas.
    """
    if eh_predador(ani):
        return obter_especie(ani)[0].upper()
    return obter_especie(ani)[0].lower()


def animal_para_str(ani):
    """ animal_para_str: animal --> str
    Recebe um animal e devolve uma cadeia de carateres que representa o animal
    """
    if eh_predador(ani):
        return obter_especie(ani) + ' [' + str(obter_idade(ani)) + '/' + str(obter_freq_reproducao(ani)) + ';'\
               + str(obter_fome(ani)) + '/' + str(obter_freq_alimentacao(ani)) + ']'
    else:
        return obter_especie(ani) + ' [' + str(obter_idade(ani)) + '/' + str(obter_freq_reproducao(ani)) + ']'


def eh_animal_fertil(ani):
    """ eh_animal_fertil: animal --> bool
    Recebe um animal e devolve True caso este se encontre em idade de reprodução, caso contrário, False
    """
    return obter_idade(ani) >= obter_freq_reproducao(ani)


def eh_animal_faminto(ani):
    """ eh_animal_faminto: animal --> bool
    Recebe um animal e devolve True caso tenha atingido o valor de fome igual ou superior à sua frequência de
    alimentação, caso contrário, False
    """
    if eh_predador(ani):
        return obter_fome(ani) >= obter_freq_alimentacao(ani)
    return False

def reproduz_animal(ani):
    """ reproduz_animal: animal --> animal
    Recebe um animal devolvendo um novo animal da mesma espécie com idade e fome igual a 0 e modificando destrutivamente
    o animal passado, como argumento de entrada, alterando a sua idade para 0
    """
    reset_idade(ani)
    return reset_fome(cria_copia_animal(ani))


# TAD prado --> R[d, r, a, p] = {'d': d, 'r': r, 'a': a, 'p': p}
def cria_prado(d, r, a, p):
    """ cria_prado: posicao, tuple, tuple, tuple --> prado
    """
    if not eh_posicao(d) or not (type(r) == type(a) == type(p) == tuple)\
        or len(a) != len(p) or len(a) == 0 or len(p) == 0:
        raise ValueError('cria_prado: argumentos invalidos')
    if len(r) != 0:        
        for roc in r:
            if not eh_posicao(roc) or obter_pos_x(roc) >= obter_pos_x(d) or obter_pos_y(roc) >= obter_pos_y(d)\
                or obter_pos_x(roc) == 0 or obter_pos_y(roc) == 0 or r.count(roc) != 1:
                raise ValueError('cria_prado: argumentos invalidos')
    for ani in a:
        if not eh_animal(ani):
            raise ValueError('cria_prado: argumentos invalidos')
    for pos in p:
        if not eh_posicao(pos) or obter_pos_x(pos) >= obter_pos_x(d) or obter_pos_y(pos) >= obter_pos_y(d)\
            or obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 or pos in r or p.count(pos) != 1:
            raise ValueError('cria_prado: argumentos invalidos')
    return {'d': d, 'r': r, 'a': a, 'p': p}


def cria_copia_prado(m):
    """ cria_copia_prado: prado --> prado
    Recebe um prado e devolve uma nova cópia do prado.
    """
    tp_roc, tp_ani, tp_pos = (), (), ()
    for roc in m['r']:
        tp_roc += (cria_copia_posicao(roc,),)
    for ani in m['a']:
        tp_ani += (cria_copia_animal(ani),)
    for pos in m['p']:
        tp_pos += (cria_copia_posicao(pos,),)
    return {'d': cria_copia_posicao(m['d']), 'r': tp_roc, 'a': tp_ani, 'p': tp_pos}


def obter_tamanho_x(m):
    """ obter_tamanho_x: prado --> int
    Recebe um prado e devolve o valor inteiro que corresponde à dimensão X do prado.
    """
    if eh_prado(m):
        return obter_pos_x(m['d']) + 1


def obter_tamanho_y(m):
    """ obter_tamanho_y: prado --> int
    Recebe um prado e devolve o valor inteiro que corresponde à dimensão Y do prado.
    """
    if eh_prado(m):
        return obter_pos_y(m['d']) + 1


def obter_numero_predadores(m):
    """ obter_numero_predadores: prado --> int
    Recebe um prado e devolve o número de animais predadores no prado.
    """
    if eh_prado(m):
        count = 0
        for ani in m['a']:
            if eh_predador(ani):
                count += 1
        return count


def obter_numero_presas(m):
    """ obter_numero_presas: prado --> int
    Recebe um prado e devolve o número de animais presas no prado.
    """
    if eh_prado(m):
        return len(m['a']) - obter_numero_predadores(m)


def obter_posicao_animais(m):
    """ obter_posicao_animais: prado --> tuplo posicoes
    Recebe um prado e devolve um tuplo contendo as posições do prado ocupadas por animais, ordenadas em ordem
    de leitura do prado.
    """
    if eh_prado(m):
        return ordenar_posicoes(m['p'])


def obter_animal(m, p):
    """ obter_animal: prado, posicao --> animal
    Recebe um prado e uma posição e devolve o animal do prado que se encontra na posição p.
    """
    if eh_prado(m) and eh_posicao(p) and p in obter_posicao_animais(m):#################
        i = m['p'].index(p)
        return m['a'][i]


def eliminar_animal(m, p):
    """ eliminar_animal: prado, posicao --> prado
    Recebe um prado e uma posição e devolve um prado m eliminando o animal da posição p deixando-a livre.
    Devolve o próprio prado.
    """
    i = m['p'].index(p)  # indice do tuplo em que a posicao e igual

    lst_ani, lst_pos = aux_tuplo_lista(m['a']), aux_tuplo_lista(m['p'])

    lst_ani.pop(i) 
    lst_pos.pop(i)

    m['a'], m['p'] = aux_lista_tuplo(lst_ani), aux_lista_tuplo(lst_pos)

    return m


def mover_animal(m, p1, p2):
    """ mover_animal: prado, posicao, posicao --> prado
    Recebe um prado e duas posições modificando destrutivamente o prado m movimentando o animal da posição
    p1 para a nova posição p2, deixando livre a posição onde se encontrava. Devolve o próprio prado.
    """
    lst_pos = aux_tuplo_lista(m['p'])
    i = lst_pos.index(p1) # indice 'i' da lista, em que o animal na posicao 'p1' se encontra
    lst_pos[i] = p2 # alterar o valor da posicao no indice 'i' da lista para 'p2'
    m['p'] = aux_lista_tuplo(lst_pos)
    return m


def inserir_animal(m, a, p):
    """ inserir_animal: prado, animal, posicao --> prado
    Recebe um prado, um animal e uma posição, modifica destrutivamente o prado m acrescentando na posição p
    do prado o animal a passado com argumento. Devolve o próprio prado.
    """
    m['a'] += (a,)
    m['p'] += (p,)
    return m


def eh_prado(arg):
    """ eh_prado: universal --> bool
    Recebe um argumento, e devolve True caso o seu argumento seja um TAD prado e False caso contrário.
    """
    if type(arg) == dict and len(arg) == 4 and 'd' in arg and 'r' in arg and 'a' in arg and 'p' in arg \
        and type(arg['r']) == type(arg['a']) == type(arg['p']) == tuple and eh_posicao(arg['d'])\
        and len(arg['a']) == len(arg['p']) != 0:
        
        if len(arg['r']) != 0:
            for roc in arg['r']:
                if not eh_posicao(roc) or roc in arg['p'] or arg['r'].count(roc) != 1 or obter_pos_x(roc) == 0\
                    or obter_pos_y(roc) == 0 or obter_pos_x(roc) >= obter_pos_x(arg['d']) or obter_pos_y(roc) >= obter_pos_y(arg['d']):
                    return False

        for pos in arg['p']:
            if not eh_posicao(pos) or arg['p'].count(pos) != 1 or obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0\
                or obter_pos_x(pos) >= obter_pos_x(arg['d']) or obter_pos_y(pos) >= obter_pos_y(arg['d']):
                return False

        for ani in arg['a']:
            if not eh_animal(ani):
                return False
        return True
    return False


def eh_posicao_animal(m, p):
    """ eh_posicao_animal: prado, posicao --> bool
    Recebe um prado e uma posição, e devolve True apenas no caso da posição p do prado estar ocupada por um
    animal.
    """
    return p in m['p']


def eh_posicao_obstaculo(m, p):
    """ eh_posicao_obstaculo: prado, posicao --> bool
    Recebe um prado e uma posição, e devolve True apenas no caso da posição p do prado corresponder a uma
    montanha ou rochedo.
    """
    x, y = obter_pos_x(p), obter_pos_y(p)
    return x == 0 or y == 0 or x == obter_pos_x(m['d']) or y == obter_pos_y(m['d']) or p in m['r']


def eh_posicao_livre(m, p):
    """ eh_posicao_livre: prado, posicao --> bool
    Recebe um prado e uma posição, e devolve True apenas no caso da posição p do prado corresponder a um
    espaço livre (sem animais, nem obstáculos).
    """
    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)


def prados_iguais(p1, p2): # REFAZER
    """ prados_iguais: prado, prado --> bool
    Recebe dois prados, e devolve True apenas se p1 e p2 forem prados e forem iguais.
    """
    if eh_prado(p1) and eh_prado(p2) and obter_tamanho_x(p1) == obter_tamanho_x(p2) and obter_tamanho_y(p1)\
        == obter_tamanho_y(p2) and obter_numero_predadores(p1) == obter_numero_predadores(p2) and \
            obter_numero_presas(p1) == obter_numero_presas(p2) and obter_posicao_animais(p1) == obter_posicao_animais(p2):
        for pos in obter_posicao_animais(p1):
            if not animais_iguais(obter_animal(p1, pos), obter_animal(p2, pos)):
                return False
        for y in range(1, obter_tamanho_y(p1)):
            for x in range(1, obter_tamanho_x(p2)):
                pos = cria_posicao(x, y)
                if not eh_posicao_obstaculo(p1, pos) == eh_posicao_obstaculo(p2, pos):
                    return False
        return True
    return False


def prado_para_str(m):
    """ prado_para_str: prado --> str
    Recebe um prado, devolve uma cadeia de caracteres que representa o prado.
    """
    prado_str = ''
    linha_sup_inf = '+' + '-' * (obter_tamanho_x(m) - 2) + '+'
    for y in range(1, obter_tamanho_y(m) - 1):
        for x in range(obter_tamanho_x(m)):
            
            if x == 0: # caso seja o inicio de uma linha
                prado_str += '|'

            elif x == obter_tamanho_x(m) - 1: # caso seja o fim de uma linha
                prado_str += '|\n'

            else:
                pos = cria_posicao(x, y)
                
                if eh_posicao_obstaculo(m, pos): # caso a posicao seja um obstaculo
                    prado_str += '@'
                
                elif eh_posicao_animal(m, pos): # caso a posicao seja um animal
                    prado_str += animal_para_char(obter_animal(m, pos))

                else: # caso seja uma posicao livre
                    prado_str += '.'

    return linha_sup_inf + '\n' + prado_str + linha_sup_inf


def obter_valor_numerico(m, p):
    """ obter_valor_numerico: prado, posicao --> int
    Recebe um prado e uma posição, e devolve o valor numérico da posição p correspondente à ordem de leitura
    no prado m.
    """
    return obter_pos_y(p) * obter_tamanho_x(m) + obter_pos_x(p)


def obter_movimento(m, p):
    """ obter_movimento: prado, posicao --> posicao
    Recebe um prado e uma posição, e devolve a posição seguinte do animal na posição p dentro do prado
    m de acordo com as regras de movimento dos animais no prado.
    """
    pos_adj = obter_posicoes_adjacentes(p)
    if eh_predador(obter_animal(m, p)):
        lst_pos_ani = list(filter(lambda pos: eh_posicao_animal(m, pos), pos_adj)) # verificar todos os animais
        lst_pos = list(filter(lambda pos: eh_presa(obter_animal(m, pos)), lst_pos_ani)) # numerar presas
        
        if len(lst_pos) == 0: # se nao existirem presas
            lst_pos = list(filter(lambda pos: eh_posicao_livre(m, pos), pos_adj)) # verifica as posicoes livres
    else: # presa
        lst_pos = list(filter(lambda pos: eh_posicao_livre(m, pos), pos_adj))
        
    if len(lst_pos) == 0: # se nao houver posicoes para onde se movimentar
        return p

    elif len(lst_pos) == 1: # quando apenas existe 1 posicao para se movimentar
        return lst_pos[0]

    return lst_pos[obter_valor_numerico(m, p) % len(lst_pos)]


# func. adicionais
def geracao(m):
    """ geracao: prado --> prado
    Recebe um prado, é uma função auxiliar que modifica o prado m fornecido como argumento de acordo com a
    evolução correspondente a uma geração completa, e devolve o próprio prado. Isto é, seguindo a ordem de
    leitura do prado, cada animal (vivo) realiza o seu turno de ação de acordo com as regras descritas.
    """
    lst = []
    for pos_inicial in obter_posicao_animais(m):
        #if pos_inicial not in lst:
        for pos in lst:
            if posicoes_iguais(pos, pos_inicial): # caso o animal se mova para uma casa que estava prester a ser analisada
                return geracao(m)
        ani = obter_animal(m, pos_inicial)
        
        pos_seg = obter_movimento(m, pos_inicial)

        lst.append(pos_seg) # guardar as posicoes para onde se movem para nao serem analisadas novamente

        aumenta_idade(ani) # quer seja presa ou predador aumenta a idade
        aumenta_fome(ani)
        
        if eh_predador(ani):
            if not posicoes_iguais(pos_inicial, pos_seg) and not eh_posicao_livre(m, pos_seg):
                eliminar_animal(m, pos_seg)
                reset_fome(ani)
        
        mover_animal(m, pos_inicial, pos_seg)

        if not posicoes_iguais(pos_inicial, pos_seg) and eh_animal_fertil(ani): # se o animal se moveu e esta fertil 
            inserir_animal(m, reproduz_animal(ani), pos_inicial)

        if eh_animal_faminto(ani):
            eliminar_animal(m, pos_seg)
    return m


def simula_ecossistema(fich, gera, modo):
    """ simula_ecossistema: str, int, bool --> tuple
    É uma função principal que permite simular o ecossistema de uma prado. Recebe um str com o nome do ficheiro,
    com os dados necessários para a criação de um prado, um int, correspondente ao número de gerações a percorrer
    e um bool, True para o modo verboso e False para o modo quiet
    """
    def aux_print(prado, conta): # funcao auxiliar para imprimir o prado e outras info no terminal
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' 
        + str(obter_numero_presas(prado)) + ' (Gen. ' + str(conta) + ')')
        print(prado_para_str(prado))
        return None
    
    tp_roc, tp_ani, tp_pos = (), (), ()
    f = open(fich, 'r')
    
    tp_dim = eval(f.readline()) # 1. linha do ficheiro, dimensao do prado, converte para tuplo
    dim = cria_posicao(tp_dim[0], tp_dim[1]) # posicao TAD da dimensao do prado
    
    roc = eval(f.readline()) # 2. linha do ficheiro, converte para tuplo com coordenadas das rochas
    for i in roc:
        tp_roc += (cria_posicao(i[0], i[1]),) # tuplo com posicoes TAD das rochas
    
    lst_ani_pos = f.readlines() # restantes linhas, lista que contem animais e as suas posicoes (em string)
    f.close()

    for j in lst_ani_pos:
        x = eval(j) # converte, 1 a 1, cada membro da lista para tuplo
        tp_ani += (cria_animal(x[0], x[1], x[2]),) # tuplo com animais TAD
        tp_pos += (cria_posicao(x[3][0], x[3][1]),) # tuplo com posicoes TAD dos animais

    prado = cria_prado(dim, tp_roc, tp_ani, tp_pos)

    if modo == False: # modo quiet
        aux_print(prado, 0) # geracao 0
        for conta in range(1, gera + 1):
            geracao(prado)
        aux_print(prado, conta) # ultima geracao

    else: # modo verboso
        aux_print(prado, 0) # geracao 0
        for conta in range(1, gera + 1):
            presas, predadores = obter_numero_presas(prado), obter_numero_predadores(prado) 
            geracao(prado)
            if obter_numero_predadores(prado) != predadores or obter_numero_presas(prado) != presas: # caso haja alteracao no n. de animais
                aux_print(prado, conta)
    return (obter_numero_predadores(prado), obter_numero_presas(prado))



simula_ecossistema('config.txt', 200, True)
