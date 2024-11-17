def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

#print(fatorial_recursivo(1000))


def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial_iterativo(1000))
