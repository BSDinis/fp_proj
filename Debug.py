from Gramatica import *


palavras = ('', 'A', 'I', 'AO', 'EO', 'RIO', 'RIE', 'CONFORTO', 'TRANSPORTAVA', 'CONSTITUCIONAL')
silabas = ('a', 'A', 'AI', 'QUE', 'TAIS', 'TRANS')
monossilabos = ('AR', 'AE', 'RIO', 'TAO')

palavras = ('AVACALHADO', 'AVENTUREIRO', 'HUMILHANTE', 'NINFOMANIACA', 'TRISSILABICO')
monossilabos = ('VIL', 'CEU', 'MEL', 'EXAME')
silabas = ('VIA', 'LEI', 'FOI', 'ID', 'UV')


def test():
    for s in silabas:
        print(s, e_silaba(s))

    for m in monossilabos:
        print(m, e_monossilabo(m))


    for p in palavras:
        print(p, e_palavra(p))


test()