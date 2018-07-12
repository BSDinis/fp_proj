with open('parte2.py') as projeto:
    linhaNumero = 0
    for linha in projeto:
        linhaNumero += 1
        for palavra in linha:
            for letra in palavra:
                if ord(letra) > 127:
                    print("Non ascii character:", palavra, "in line", linhaNumero)
                    break

input()
