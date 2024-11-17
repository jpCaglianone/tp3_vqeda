def eh_palindromo(palavra, inicio=0, fim=None):
    if fim is None:
        fim = len(palavra) - 1
    if inicio >= fim:
        return True
    if palavra[inicio] != palavra[fim]:
        return False
    return eh_palindromo(palavra, inicio + 1, fim - 1)

print(eh_palindromo("radar"))
print(eh_palindromo("python"))
print(eh_palindromo("arara"))
print(eh_palindromo("caligola"))

