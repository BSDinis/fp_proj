from parte1 import e_palavra

# Lista de letras maiusculas
maiusculas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', \
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


## TAD palavra_potencial

# Representacao interna: cadeia de caracteres de letras maiusculas

# Construtor
def cria_palavra_potencial(string, letras):
    '''construtor do TAD palavra_potencial
    cria_palavra_potencial: string x tuplo -> palavra_potencial'''

    codigo = e_par_para_potencial(string, letras)
    if codigo == 0:
        return string
    elif codigo == 1:
        raise ValueError("cria_palavra_potencial:a palavra nao e valida.")
    else:
        raise ValueError("cria_palavra_potencial:argumentos invalidos.")


# Funcao auxiliar
# verifica se uma cadeia de caracteres e um tuplo podem ser usados para
# criar uma palavra_potencial
def e_par_para_potencial(arg1, arg2):
    '''funcao auxiliar
    e_par_para_potencial: universal x universal -> logico'''

    if isinstance(arg1, str) and isinstance(arg2, tuple):
        for c in arg1:
            if c not in maiusculas:  # verifica que a string so tem maiusculas
                return 2  # codigo argumentos invalidos

        for c in arg2:
            if c not in maiusculas:  # verifica que o tuplo so tem maiusculas
                return 2  # codigo argumentos invalidos

            i = 0
            while i < len(arg1):
                if arg1[i] == c:
                    arg1 = arg1[:i] + arg1[i + 1:]  # retira o caracter da string
                    i = len(arg1)  # forca a saida, so pode retirar um caracter de cada vez

                i = i + 1

        if len(arg1) == 0:  # nao pode haver digitos que nao estao no tuplo
            return 0  # codigo de que passou
        else:
            return 1  # a palavra nao e valida

    else:
        return 2  # codigo argumentos invalidos


# Seletor
def palavra_tamanho(palavra):
    '''seletor do TAD palavra_potencial
    palavra_tamanho: palavra_potencial -> inteiro'''

    return len(palavra)


# Reconhecedor
def e_palavra_potencial(arg):
    '''reconhecedor do TAD palavra_potencial
    e_palavra_potencial: universal -> logico'''

    if isinstance(arg, str):
        for c in arg:
            if c not in maiusculas:
                return False

        return True
    else:
        return False


# Testes
def palavras_potenciais_iguais(p1, p2):
    '''teste de igualdade do TAD palavra_potencial
    palavras_potenciais_iguais: palavra_potencial x palavra_potencial -> logico'''

    return p1 == p2


def palavra_potencial_menor(p1, p2):
    '''teste de ordem do TAD palavra_potencial
    palavra_potencial_menor: palavra_potencial x palavra_potencial -> logico'''

    l1 = palavra_tamanho(p1)
    l2 = palavra_tamanho(p2)
    l = min(l1, l2)

    for i in range(l):
        if p1[i] < p2[i]:
            return True
        elif p1[i] > p2[i]:
            return False

    return l1 < l2


# Funcoes de Alto Nivel
def palavra_potencial_para_cadeia(p):
    '''funcao de alto nivel do TAD palavra_potencial
    Escreve a string correspondente a palavra_potencial'''

    if e_palavra_potencial(p):
        return p
    else:
        raise ValueError("palavra_potencial_para_cadeia:argumentos invalidos.")


## TAD conjunto_palavras
# Representacao interna: lista de palavras_potenciais 

# Construtor
def cria_conjunto_palavras():
    '''construtor do TAD conjunto_palavras
    retorna conjunto vazio

    cria_conjunto_palavras: -> conjunto_palavras'''

    return list()


# Seletores

# Seletor tamanho
def numero_palavras(c):
    '''seletor do TAD conjunto_palavras
    numero_palavras: conjunto_palavras -> inteiro'''

    return len(c)


# Seletor do subconjunto por tamanho
def subconjunto_por_tamanho(c, l):
    '''seletor do TAD conjunto_palavras
    subconjunto_por_tamanho: conjunto_palavras x inteiro -> conjunto_palavras'''

    subc = list()
    for palavra in c:
        if palavra_tamanho(palavra) == l:
            subc = subc + [palavra]

    return subc


# Reconhecedor
def e_conjunto_palavras(arg):
    '''reconhecedor do TAD conjunto_palavras
    e_conjunto_palavras: universal -> logico'''

    if isinstance(arg, list):
        for palavra in arg:
            if not e_palavra_potencial(palavra):
                return False

        return True
    else:
        return False


# Testes
def conjuntos_palavras_iguais(c1, c2):
    '''teste de igualdade do TAD conjunto_palavras
    conjuntos_palavras_iguais: conjunto_palavras x conjunto_palavras -> logico'''

    if numero_palavras(c1) == numero_palavras(c2):
        for palavra in c1:
            if palavra not in c2:
                return False

        return True

    else:
        return False


def pertence_conjunto(c, palavra):
    '''teste de pertenca do TAD conjunto_palavras
    pertence_conjunto: conjunto_palavras x palavra_potencial -> logico'''

    for p in c:
        if palavras_potenciais_iguais(palavra, p):
            return True

    return False


# Modificadores
def acrescenta_palavra(c, palavra):
    '''modificador do TAD conjunto_palavras
    acrescenta_palavra: conjunto_palavras x palavra_potencial -> '''

    if e_conjunto_palavras(c) and e_palavra_potencial(palavra):
        if not pertence_conjunto(c, palavra):
            c += [palavra]
    else:
        raise ValueError("acrescenta_palavra:argumentos invalidos.")

def remove_palavra(c, palavra):
    '''modificador do TAD conjunto_palavras
    remove_palavra: conjunto_palavras x palavra_potencial -> '''

    if e_conjunto_palavras(c) and e_palavra_potencial(palavra):
        i = numero_palavras(c) - 1
        while i >= 0:
            if palavras_potenciais_iguais(c[i], palavra):
                del(c[i])
            i = i - 1

    else:
        raise ValueError("remove_palavra:argumentos invalidos")



# Funcao de Alto Nivel
def conjunto_palavras_para_cadeia(c):
    '''transformador do TAD conjunto_palavras
    conjunto_palavras_para_cadeia: conjunto_palavras -> cad. caracteres'''
    def filtra_plicas(string):
        '''remove as plicas de uma string
        filtra_plicas: cad. caracteres -> cad. caracteres'''
        filtrada = str()
        for c in string:
            if c != "'":
                filtrada = filtrada + c

        return filtrada

    # Funcoes auxiliares; ordenacao de uma lista
    def ordena_subconjunto(sub):
        def merge(l1, l2, cmp):
            '''junta duas listas ordenadas numa lista ordenada;
            funcao auxiliar do merge_sort
            utiliza a funcao de comparacao de input
            
            merge: lista x lista x funcao -> lista'''

            res = list()
            i = 0
            j = 0
            while i < len(l1) and j < len(l2):
                if cmp(l1[i], l2[j]):
                    res = res + [l1[i]]
                    i = i + 1
                else:
                    res = res + [l2[j]]
                    j = j + 1

            while i < len(l1):
                res = res + [l1[i]]
                i = i + 1

            while j < len(l2):
                res = res + [l2[j]]
                j = j + 1

            return res

        def merge_sort(l, cmp):
            '''merge_sort
            ordenacao por divide and conquer
        
            merge_sort: lista x funcao -> lista'''

            if len(l) <= 1:
                return l
            else:
                m = len(l) // 2
                return merge(merge_sort(l[:m], cmp), merge_sort(l[m:], cmp), cmp)

        return merge_sort(sub, palavra_potencial_menor)

    # Fim das funcoes auxiliares

    if e_conjunto_palavras(c):
        cont = numero_palavras(c)
        l = 0
        cad = str()
        while cont > 0:
            sub = ordena_subconjunto(subconjunto_por_tamanho(c, l))

            if len(sub) > 0:
                cont = cont - len(sub)
                cad = cad + str(l) + '->' + str(sub) + ';'

            l = l + 1

        cad = '[' + cad[:-1] + ']'  # substitui o ultimo ';'
        return filtra_plicas(cad)


## TAD Jogador
# Representacao interna: lista: [<nome>, <pontuacao>, <validas>, <invalidas>]

# Construtor
def cria_jogador(nome):
    '''construtor do TAD jogador
    cria_jogador: cad. caracteres -> jogador'''

    if isinstance(nome, str):
        val = cria_conjunto_palavras()
        inval = cria_conjunto_palavras()
        pont = 0
        return [nome, pont, val, inval]
    else:
        raise ValueError("cria_jogador:argumento invalido.")


# Seletores
def jogador_nome(jog):
    '''seletor do TAD jogador
    jogador_nome: jogador -> cad. caracteres'''

    return jog[0]


def jogador_pontuacao(jog):
    '''seletor do TAD jogador
    jogador_pontuacao: jogador -> inteiro'''

    return jog[1]


def jogador_palavras_validas(jog):
    '''seletor do TAD jogador
    jogador_palavras_validas: jogador -> conjunto_palavras'''

    return jog[2]


def jogador_palavras_invalidas(jog):
    '''seletor do TAD jogador
    jogador_palavras_validas: jogador -> conjunto_palavras'''

    return jog[3]


# Reconhecedor
def e_jogador(arg):
    '''reconhecedor do TAD jogador
    e_jogador: universal -> logico'''

    return isinstance(arg, list) and len(arg) == 4 and \
           isinstance(arg[0], str) and \
           isinstance(arg[1], int) and \
           e_conjunto_palavras(arg[2]) and \
           e_conjunto_palavras(arg[3])


# Modificadores
def atualiza_pontuacao(jog, val):
    '''modificador do TAD jogador
    atualiza_pontuacao: jogador x inteiro ->'''

    if isinstance(val, int) and e_jogador(jog):
        jog[1] = jog[1] + val
    else:
        raise ValueError("atualiza_pontuacao:argumentos invalidos")


def adiciona_palavra_valida(jog, palavra):
    '''modificador do TAD jogador
    adiciona_palavra_valida: jogador x palavra_potencial ->'''

    if e_jogador(jog) and e_palavra_potencial(palavra):
        if not pertence_conjunto(jogador_palavras_validas(jog), palavra):
            acrescenta_palavra(jogador_palavras_validas(jog), palavra)
            atualiza_pontuacao(jog, palavra_tamanho(palavra))
    else:
        raise ValueError("adiciona_palavra_valida:argumentos invalidos.")


def adiciona_palavra_invalida(jog, palavra):
    '''modificador do TAD jogador
    adiciona_palavra_invalida: jogador x palavra_potencial ->'''

    if e_jogador(jog) and e_palavra_potencial(palavra):
        if not pertence_conjunto(jogador_palavras_invalidas(jog), palavra):
            acrescenta_palavra(jogador_palavras_invalidas(jog), palavra)
            atualiza_pontuacao(jog, -palavra_tamanho(palavra))
    else:
        raise ValueError("adiciona_palavra_invalida:argumentos invalidos.")


# Funcao alto nivel
def jogador_para_cadeia(jog):
    '''funcao de alto nivel do TAD jogador
    Devolve a string correspondente a um jogador
        
    jogador_para_cadeia: palavra_potencial -> cad. caracteres'''

    if e_jogador(jog):
        return 'JOGADOR ' + jogador_nome(jog) + ' PONTOS=' + str(jogador_pontuacao(jog)) + \
               ' VALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_validas(jog)) + \
               ' INVALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_invalidas(jog))
    else:
        raise ValueError("jogador_para_cadeia:argumento invalido.")


## Funcoes Adicionais

# Gerador de palavras_validas
def gera_todas_palavras_validas(letras):
    '''funcao adicional
    gera todas as palavras validas, segundo a gramatica, que podem
    ser construidas a partir do tuplo de letras que e introduzido

    gera_todas_palavras_validas: tuplo -> conjunto_palavras'''

    lista_palavras = list()
    for ch in letras:
        if ch not in lista_palavras:
            lista_palavras = lista_palavras + [ch]

    for n in range(1, len(letras)):
        l = len(lista_palavras)
        for i in range(l):
            for ch in letras:
                palavra = lista_palavras[i] + ch
                if e_par_para_potencial(palavra, letras) == 0 and palavra not in lista_palavras:
                    lista_palavras = lista_palavras + [palavra]

    c = cria_conjunto_palavras()
    for palavra in lista_palavras:
        if e_palavra(palavra):
            acrescenta_palavra(c, cria_palavra_potencial(palavra, letras))

    return c


# Guru Multyplayer
def guru_mj(letras):
    '''funcao adicional
    estrutura geral do jogo

    guru_mj: tuplo ->'''

    def inscricao():
        '''funcao auxiliar
        devolve a lista dos jogadores no jogo

        inscricao: -> lista'''

        print("Introduza o nome dos jogadores (-1 para terminar)...")

        jogadores = list()
        nome = str()
        n = 1
        while nome != '-1':
            pedido = 'JOGADOR ' + str(n) + ' -> '
            nome = input(pedido)
            if nome != '-1':
                jogadores = jogadores + [cria_jogador(nome)]
                n = n + 1

        return jogadores

    def recebe_proposta(jog, letras):
        '''funcao auxiliar
        recebe uma proposta de palavra do jogador

        recebe_proposta: jogador x tuplo -> palavra_potencial'''
        return cria_palavra_potencial(input('JOGADOR ' + jogador_nome(jog) + ' -> '), letras)

    def ganho(por_descobrir):
        '''funcao auxiliar
        verifica se o jogo foi ganho

        ganho: conjunto_palavras -> logico'''

        return numero_palavras(por_descobrir) == 0

    def vencedores(jogadores):
        '''funcao auxiliar
        dada a lista dos jogadores, verifica qual(quais)
        ganhou (empataram em primeiro lugar)

        vencedores: lista -> lista'''

        if len(jogadores) > 0:
            vencedores = [jogadores[0]]
            for i in range(1, len(jogadores)):
                if jogador_pontuacao(jogadores[i]) > jogador_pontuacao(vencedores[0]):
                    vencedores = [jogadores[i]]
                elif jogador_pontuacao(jogadores[i]) == jogador_pontuacao(vencedores[0]):
                    vencedores = vencedores + [jogadores[i]]

        return vencedores

    ## Fim das funcoes auxiliares

    print("Descubra todas as palavras geradas a partir das letras:")
    print(letras)
    jogadores = inscricao()
    palavras_validas = gera_todas_palavras_validas(letras)
    por_descobrir = gera_todas_palavras_validas(letras)
    i = 0
    n_jog = len(jogadores)

    while not ganho(por_descobrir):
        print("JOGADA", i + 1, "- Falta descobrir", numero_palavras(por_descobrir), "palavras")
        proposta = recebe_proposta(jogadores[i % n_jog], letras)
        cad = palavra_potencial_para_cadeia(proposta) + " - palavra "

        if pertence_conjunto(palavras_validas, proposta) and pertence_conjunto(por_descobrir, proposta):
            print(cad + "VALIDA")
            adiciona_palavra_valida(jogadores[i % n_jog], proposta)
            remove_palavra(por_descobrir, proposta)
        elif pertence_conjunto(palavras_validas, proposta):
            print(cad + "VALIDA")
        else:
            print(cad + "INVALIDA")
            adiciona_palavra_invalida(jogadores[i % n_jog], proposta)

        i = i + 1

    venc = vencedores(jogadores)
    if len(venc) == 1:
        print("FIM DE JOGO! O jogo terminou com a vitoria do jogador " + jogador_nome(venc[0]) + \
              " com " + str(jogador_pontuacao(venc[0])) + " pontos.")
    else:
        print("FIM DE JOGO! O jogo terminou em empate.")

    for jog in jogadores:
        print(jogador_para_cadeia(jog))

    return

