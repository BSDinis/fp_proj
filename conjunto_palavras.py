# Lista de letras maiusculas
maiusculas = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', \
				'P','Q','R','S','T','U','V','W','X','Y','Z')


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

	print("Reconhecedor", arg)
	if isinstance(arg, (list, tuple)):
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
		return  False

def pertence_conjunto(c, palavra):
	'''teste de pertenca do TAD conjunto_palavras
	pertence_conjunto: conjunto_palavras x palavra_potencial -> logico'''

	for p in c:
		if palavras_potenciais_iguais(palavra, p):
			return True

	return False

# Modificador
def acrescenta_palavra(c, palavra):
	'''modificador do TAD conjunto_palavras
	acrescenta_palavra: conjunto_palavras x palavra_potencial -> '''

	if e_conjunto_palavras(c) and e_palavra_potencial(palavra):
		if not pertence_conjunto(c, palavra):
			c += [palavra]
	else:
		raise ValueError("acrescenta_palavra:argumentos invalidos.")


# Funcao de Alto Nivel
def conjunto_palavras_para_cadeia(c):
	'''transformador do TAD conjunto_palavras
	conjunto_palavras_para_cadeia: conjunto_palavras -> cad. caracteres'''

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

	#Fim das funcoes auxiliares

	if e_conjunto_palavras(c):
		cont = numero_palavras(c)
		l = 0
		cad = '['
		while cont > 0:
			sub = ordena_subconjunto(subconjunto_por_tamanho(c, l))

			if len(sub) > 0:
				cont = cont - len(sub)
				cad = cad + str(l) + '->' + str(sub) + ';'

			l = l + 1

		cad = cad[:-1] + ']' # substitui o ultimo ';'
		return cad



# Testing

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

	return

#test_palavra_potencial()
#test_conjunto_palavras()


