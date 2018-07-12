# Lista de letras maiusculas
maiusculas = ('A','B','C','D','E','F','G','H','I','J','L','M','N','O', \
				'P','Q','R','S','T','U','V','X','Z')


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
			if c not in maiusculas: # verifica que a string so tem maiusculas
				return 2 # codigo argumentos invalidos

		for c in arg2:
			if c not in maiusculas: # verifica que o tuplo so tem maiusculas
				return 2 # codigo argumentos invalidos

			i = 0
			while i < len(arg1):
				if arg1[i] == c:
					arg1 = arg1[:i] + arg1[i + 1:] # retira o caracter da string
					i = len(arg1) # forca a saida, so pode retirar um caracter de cada vez

				i = i + 1

		if len(arg1) == 0: # nao pode haver digitos que nao estao no tuplo
	   		return 0 # codigo de que passou
		else:
			return 1 # a palavra nao e valida

	else:
		return 2 # codigo argumentos invalidos
				

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
	Devolve a string correspondente a palavra_potencial
        
        palavra_potencial_para_cadeia: palavra_potencial -> cad. caracteres'''

	if e_palavra_potencial(p):
		return p
	else:
		raise ValueError("palavra_potencial_para_cadeia:argumentos invalidos.")


# Testing
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

#test_palavra_potencial()







