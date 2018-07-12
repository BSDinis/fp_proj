# 89416 Baltasar Azevedo e Silva Dinis

# Todas as funcoes que sao da forma e_<simbolo nao terminal> (<snt>)
# Verificam se a cadeia de carateres introduzida e o <snt>
# correspondente de acordo com a gramatica apresentada
#
# Excepcao: funcao auxiliar e_silabas
#
# Em algumas funcoes, utiliza-se a variavel 'valido', do tipo logico, para 
# facilitar a leitura do codigo, separando a disjuncao de condicoes por varias
# linhas


# e_palavra
# Funcoes auxiliares:
#   *e_silaba (len em [1, 5])
#   *e_monossilabo (len em [1, 3])
#   *e_silaba_final (len em [2, 5])

def e_palavra(cc):
    """Utilizacao: e_palavra(<cadeia de caracteres>)
    Verifica se o input e uma palavra valida
    e_palavra: cad. caracteres -> booleano
    Gramatica: <palavra>::=<monossilabo>|<silaba> * <silaba_final>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_palavra:argumento invalido")

    #verifica se no segmento final existe uma silaba final e se o resto
    #da cadeia de caracteres e composta por zero ou mais silabas
    #
    #verifica em cada comprimento possivel para a silaba final
    max_len = max(5, len(cc))  # maximo do comprimento maximo da silaba final e do comprimento do input
    min_len = 2  # comprimento minimo da silaba final
    valido = False
    for i in range(-max_len, -min_len + 1):
        valido = valido or (e_silabas(cc[:i]) and e_silaba_final(cc[i:]))

    valido = valido or e_monossilabo(cc)
    return valido


# e_silabas: funcao auxiliar
def e_silabas(cc):
    """Utilizacao: e_silabas(<cadeia de caracteres>)
    Verifica se o input e um conjunto de silabas validas
    e_silabas: cad. caracteres -> booleano"""
    
    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silabas:argumento invalido")
    elif cc == '':
    	return True

    max_len = max(5, len(cc)) # maximo do comprimento maximo da silaba e do comprimento do input
    min_len = 1 # comprimento minimo da silaba
    valido = False

    for i in range(min_len, max_len + 1):
        #testa para todas as posicoes possiveis do separador (i)
        valido = valido or (e_silaba(cc[:i]) and e_silabas(cc[i:]))

    return valido

# e_silaba
# Funcoes auxiliares:
#   *e_vogal
#   *e_silaba_2
#   *e_silaba_3
#   *e_silaba_4
#   *e_silaba_5
def e_silaba(cc):
    """Utilizacao: e_silaba(<cadeia de caracteres>)
    Verifica se o input e uma silaba valida
    e_silaba: cad. caracteres -> booleano
    Gramatica: <silaba>::=<vogal>|<silaba_2>|<silaba_3>|<silaba_4>|<silaba_5>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba:argumento invalido")
 
    return e_vogal(cc) or e_silaba_2(cc) or e_silaba_3(cc) or e_silaba_4(cc) or e_silaba_5(cc)


def e_silaba_2(cc):
    """Utilizacao: e_silaba_2(<cadeia de caracteres>)
    Verifica se o input e uma silaba_2 valida
    e_silaba_2: cad. caracteres -> booleano
    Gramatica: <silaba_2>::=<par_vogais>|<consoante><vogal>|<vogal><consoante_final>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba_2:argumento invalido")
     
    #verifica o comprimento do input
    if len(cc) != 2:
        return False

    valido = e_par_vogais(cc)
    valido = valido or (e_consoante(cc[0]) and e_vogal(cc[1]))
    valido = valido or (e_vogal(cc[0]) and e_consoante_final(cc[1]))
    return valido


def e_silaba_3(cc):
    """Utilizacao: e_silaba_3(<cadeia de caracteres>)
    Verifica se o input e uma silaba_3 valida
    e_silaba_3: cad. caracteres -> booleano
    Gramatica: <silaba_3>::=QUA|QUE|QUI|GUE|GUI|<vogal>NS|<consoante><par_vogais>
                  |<consoante><vogal><consoante_final>
                  |<par_vogais><consoante_final>
                  |<par_consoantes><vogal>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba_3:argumento invalido")
    
    #verifica o comprimento do input
    if len(cc) != 3:
        return False

    valido = (e_vogal(cc[0]) and cc[1:3] == 'NS')
    valido = valido or (e_consoante(cc[0]) and e_par_vogais(cc[1:3]))
    valido = valido or (e_consoante(cc[0]) and e_vogal(cc[1]) and e_consoante_final(cc[2]))
    valido = valido or (e_par_vogais(cc[0:2]) and e_consoante_final(cc[2]))
    valido = valido or (e_par_consoantes(cc[0:2]) and e_vogal(cc[2]))
    valido = valido or cc in ('QUA', 'QUE', 'QUI', 'GUE', 'GUI')
    return valido


def e_silaba_4(cc):
    """Utilizacao: e_silaba_4(<cadeia de caracteres>)
    Verifica se o input e uma silaba_4 valida
    e_silaba_4: cad. caracteres -> booleano
    Gramatica: <silaba_4>::=<par_vogais>NS|<consoante><vogal>NS|<consoante><vogal>IS
                  |<par_consoantes><par_vogais>
                  |<consoante><par_vogais><consoante_final>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba:argumento invalido")
    
    #verifica o comprimento do input
    if len(cc) != 4:
        return False

    valido = e_par_vogais(cc[:2]) and cc[2:4] == 'NS'
    valido = valido or (e_consoante(cc[0]) and e_vogal(cc[1]) and (cc[2:4] == 'NS' or cc[2:] == 'IS'))
    valido = valido or (e_par_consoantes(cc[:2]) and e_par_vogais(cc[2:4]))
    valido = valido or (e_consoante(cc[0]) and e_par_vogais(cc[1:3]) and e_consoante_final(cc[3]))
    return valido


def e_silaba_5(cc):
    """Utilizacao: e_silaba_5(<cadeia de caracteres>)
    Verifica se o input e uma silaba_5 valida
    e_silaba_5: cad. caracteres -> booleano
    Gramatica: <silaba_5>::=<par_consoantes><vogal>NS"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba_5:argumento invalido")
    
    #verifica o comprimento do input
    if len(cc) != 5:
        return False

    return e_par_consoantes(cc[:2]) and e_vogal(cc[2]) and cc[3:5] == 'NS'


# e_silaba_final (comprimento entre 2 e 5)
def e_silaba_final(cc):
    """Utilizacao: e_silaba_final(<cadeia de caracteres>)
    Verifica se o input e uma silaba final valida
    e_silaba_final: cad. caracteres -> booleano
    Gramatica: <silaba_final>::=<monossilabo_2>|<monossilabo_3>|<silaba_4>|<silaba_5>"""
    
    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_silaba_final:argumento invalido")
    
    return e_monossilabo_2(cc) or e_monossilabo_3(cc) or e_silaba_4(cc) or e_silaba_5(cc)


# e_monossilabo
#
# Funcoes auxiliares:
#   *e_vogal_palavra
#   *e_monossilabo_2
#   *e_monossilabo_3
def e_monossilabo(cc):
    """Utilizacao: e_monossilabo(<cadeia de caracteres>)
    Verifica se o input e um monossilabo valido
    e_monossilabo: cad. caracteres -> booleano
    Gramatica: <monossilabo>::=<vogal_palavra>|<monossilabo_2>|<monossilabo_3>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_monossilabo:argumento invalido")
    
    return e_vogal_palavra(cc) or e_monossilabo_2(cc) or e_monossilabo_3(cc)


def e_monossilabo_2(cc):
    """Utilizacao: e_monossilabo_2(<cadeia de caracteres>)
    Verifica se o input e um monossilabo_2 valido
    e_monossilabo_2: cad. caracteres -> booleano
    Gramatica: <monossilabo_2>::=AR|IR|EM|UM|<vogal_palavra>S|<ditongo_palavra>
                      |<consoante_freq><vogal>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_monossilabo2:argumento invalido")
    
    #verifica o comprimento do input
    if len(cc) != 2:
        return False

    valido = e_vogal_palavra(cc[0]) and cc[1] == 'S'
    valido = valido or e_ditongo_palavra(cc)
    valido = valido or (e_consoante_freq(cc[0]) and e_vogal(cc[1]))
    valido = valido or cc in ('AR', 'IR', 'EM', 'UM')
    return valido


def e_monossilabo_3(cc):
    """Utilizacao: e_monossilabo_3(<cadeia de caracteres>)
    Verifica se o input e um monossilabo_3 valido
    e_monossilabo_3: cad. caracteres -> booleano
    Gramatica: <monossilabo_3>::=<consoante><vogal><consoante_terminal>
                          |<consoante><ditongo>
                          |<par_vogais><consoante_terminal>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_monossilabo_3:argumento invalido")
    
    #verifica o comprimento do input
    if len(cc) != 3:
        return False

    valido = e_consoante(cc[0]) and ((e_vogal(cc[1]) and e_consoante_terminal(cc[2])) or e_ditongo(cc[1:3]))
    valido = valido or (e_par_vogais(cc[:2]) and e_consoante_terminal(cc[2]))
    return valido


def e_consoante(cc):
    """Utilizacao: e_consoante(<cadeia de caracteres>)
    Verifica se o input e uma consoante valida
    e_consoante: cad. caracteres -> booleano
    Gramatica: <consoante>::=B|C|D|F|G|H|J|L|M|N|P|Q|R|S|T|V|X|Z"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_consoante:argumento invalido")

    return cc in ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z')


def e_consoante_final(cc):
    """Utilizacao: e_consoante_final(<cadeia de caracteres>)
    Verifica se o input e uma consoante_final valida
    e_consoante_final: cad. caracteres -> booleano
    Gramatica: <consoante_final>::=N|P|<consoante_terminal>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_consoante_final:argumento invalido")

    return cc in ('N', 'P') or e_consoante_terminal(cc)


def e_consoante_terminal(cc):
    """Utilizacao: e_consoante_terminal(<cadeia de caracteres>)
    Verifica se o input e uma consoante_terminal valida
    e_consoante_terminal: cad. caracteres -> booleano
    Gramatica: <consoante_terminal>::=L|M|R|S|X|Z"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_consoante_terminal:argumento invalido")
 
    return cc in ('L', 'M', 'R', 'S', 'X', 'Z')



def e_consoante_freq(cc):
    """Utilizacao: e_consoante_freq(<cadeia de caracteres>)
    Verifica se o input e uma consoante_freq valida
    e_consoante_freq: cad. caracteres -> booleano
    Gramatica: <consoante_freq>::=D|L|M|N|P|R|S|T|V"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_consoante_freq:argumento invalido")
    
    return cc in ('D', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V')


def e_par_consoantes(cc):
    """Utilizacao: e_par_consoantes(<cadeia de caracteres>)
    Verifica se o input e um par_consoantes valido
    e_par_consoantes: cad. caracteres -> booleano
    Gramatica: <par_consoantes>::=BR|CR|FR|GR|PR|TR|VR|BL|CL|FL|GL|PL"""
 
    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_par_constantes:argumento invalido")
    
    return cc in ('BR', 'CR', 'FR', 'GR', 'PR', 'TR', 'VR', 'BL', 'CL', 'FL', 'GL', 'PL')


def e_vogal(cc):
    """Utilizacao: e_vogal(<cadeia de caracteres>)
    Verifica se o input e uma vogal valida
    e_vogal: cad. caracteres -> booleano
    Gramatica: <vogal>::=I|U|<vogal_palavra>"""
 
    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_vogal:argumento invalido")
    
    return cc in ('I', 'U') or e_vogal_palavra(cc)


def e_vogal_palavra(cc):
    """Utilizacao: e_vogal_palavra(<cadeia de caracteres>)
    Verifica se o input e uma vogal_palavra valida
    e_vogal_palavra: cad. caracteres -> booleano
    Gramatica: <vogal_palavra>::=<artigo_def>|E"""
 
    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_vogal_palavra:argumento invalido")
    
    return cc == 'E' or e_artigo_def(cc)


def e_par_vogais(cc):
    """Utilizacao: e_par_vogais(<cadeia de caracteres>)
    Verifica se o input e um par_vogais valido
    e_par_vogais: cad. caracteres -> booleano
    Gramatica: <par_vogais>::=<ditongo>|IA|IO""" 

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_par_vogais:argumento invalido")
    
    return  e_ditongo(cc) or cc in ('IA', 'IO')


def e_ditongo(cc):
    """Utilizacao: e_ditongo(<cadeia de caracteres>)
    Verifica se o input e um ditongo valido
    e_ditongo: cad. caracteres -> booleano
    Gramatica: <ditongo>::=AE|AU|EI|OE|OI|IU|<ditongo_palavra>"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_ditongo:argumento invalido")
    
    return cc in ('AE', 'AU', 'EI', 'OE', 'OI', 'IU') or e_ditongo_palavra(cc)


def e_ditongo_palavra(cc):
    """Utilizacao: e_ditongo_palavra(<cadeia de caracteres>)
    Verifica se o input e um ditongo_palavra valido
    e_ditongo_palavra: cad. caracteres -> booleano
    Gramatica: <ditongo_palavra>::=AI|AO|EU|OU"""        

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_ditongo_palavra:argumento invalido")
    
    return cc in ('AI', 'AO', 'EU', 'OU')


def e_artigo_def(cc):
    """Utilizacao: e_artigo_def(<cadeia de caracteres>)
       Verifica se o input e um artigo_def valido
       e_artigo_def: cad. caracteres -> booleano
       Gramatica: <artigo_def>::=A|O"""

    #faz a verificacao do input
    if not isinstance(cc, str):
        raise ValueError("e_artigo_def:argumento invalido")
    
    return cc in ('A', 'O')
