from parte2 import *


# Testing

def test(code):
    # Palavra_potencial
    def test_palavra_potencial():
        conjunto = ('a', 'E', 'L', 'M', 'T')
        try:
            p = cria_palavra_potencial("METa", conjunto)
        except ValueError:
            print("Falhou como esperado1")

        conjunto = ('A', 'E', 'L', 'M', 'T')
        try:
            p = cria_palavra_potencial("1META", conjunto)
        except ValueError:
            print("Falhou como esperado2")

        try:
            p = cria_palavra_potencial("AMETA", conjunto)
        except ValueError:
            print("Falhou como esperado3")

        p = cria_palavra_potencial("META", conjunto)
        print(palavra_tamanho(p))
        print(e_palavra_potencial(p))
        print(e_palavra_potencial("1META"))
        print(e_palavra_potencial("mETA"))

        p1 = cria_palavra_potencial("META", conjunto)
        p2 = cria_palavra_potencial("TELA", conjunto)
        p3 = cria_palavra_potencial("", conjunto)
        print(palavras_potenciais_iguais(p, p))
        print(palavras_potenciais_iguais(p, p1))
        print(palavras_potenciais_iguais(p, p2))
        print(palavra_potencial_menor(p1, p2))
        print(palavra_potencial_menor(p2, p1))
        print(palavra_potencial_menor(p2, p2))
        print(palavra_potencial_para_cadeia(p))
        print(palavra_potencial_para_cadeia(p1))
        print(palavra_potencial_para_cadeia(p2))
        print(palavra_potencial_para_cadeia(p3))

        return

    # Conjunto_Palavras
    def test_conjunto_palavras():
        letras = ("A", "E", "L")
        p1 = cria_palavra_potencial("A", letras)
        p2 = cria_palavra_potencial("E", letras)
        p3 = cria_palavra_potencial("LA", letras)
        p4 = cria_palavra_potencial("ELA", letras)

        try:
            c = cria_conjunto_palavras()
        except ValueError:
            print("Falhou e nao devia")

        try:
            acrescenta_palavra(c, p3)
            acrescenta_palavra(c, p4)
            acrescenta_palavra(c, p1)
            acrescenta_palavra(c, p2)
        except ValueError:
            print("Falhou e nao devia")

        print(conjunto_palavras_para_cadeia(c))
        print(subconjunto_por_tamanho(c, 1))

        c = cria_conjunto_palavras()
        p1 = cria_palavra_potencial('A', ('A',))
        p2 = cria_palavra_potencial('', ())
        acrescenta_palavra(c, p1)
        acrescenta_palavra(c, p2)
        print(conjunto_palavras_para_cadeia(c))

        c = cria_conjunto_palavras()
        p1 = cria_palavra_potencial('A', ('A',))
        p2 = cria_palavra_potencial('C', ('C',))
        acrescenta_palavra(c, p1)
        acrescenta_palavra(c, p2)
        print(conjunto_palavras_para_cadeia(c))

        return

    # Jogador
    def test_jogador():
        letras = ("A", "E", "L")
        p1 = cria_palavra_potencial("ELA", letras)
        p2 = cria_palavra_potencial("AL", letras)
        jog = cria_jogador("joao")
        adiciona_palavra_valida(jog, p1)
        print(jogador_pontuacao(jog))
        adiciona_palavra_valida(jog, p1)
        print(jogador_pontuacao(jog))
        adiciona_palavra_invalida(jog, p2)
        print(jogador_para_cadeia(jog))
        return

    # Funcoes Adicionais

    def test_func_adicionais():
        letras = ('M', 'A', 'S', 'S', 'A')
        c = gera_todas_palavras_validas(letras)
        conjunto_palavras_para_cadeia(c)
        print(numero_palavras(c))
        letras = ('M', 'A', 'S', 'A')
        c = gera_todas_palavras_validas(letras)
        conjunto_palavras_para_cadeia(c)
        print(numero_palavras(c))
        letras = ('M', 'A', 'S')
        c = gera_todas_palavras_validas(letras)
        conjunto_palavras_para_cadeia(c)
        print(numero_palavras(c))
        letras = ('M', 'A', 'S', 'K')
        c = gera_todas_palavras_validas(letras)
        conjunto_palavras_para_cadeia(c)
        print(numero_palavras(c))

        guru_mj(("A", "M"))

    if code == 1:
        test_palavra_potencial()
    elif code == 2:
        test_conjunto_palavras()
    elif code == 3:
        test_jogador()
    elif code == 4:
        test_func_adicionais()


test(4)
