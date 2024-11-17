def quicksort(vetor, inicio, fim):
    if inicio < fim:
        pi = particionar(vetor, inicio, fim)
        quicksort(vetor, inicio, pi - 1)
        quicksort(vetor, pi + 1, fim)

def particionar(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if vetor[j] < pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1


# Teste 1
vetor1 = [10, 7, 8, 9, 1, 5]
quicksort(vetor1, 0, len(vetor1) - 1)
print("Vetor ordenado (Teste 1):", vetor1)

# Teste 2
vetor2 = [1, 2, 3, 4, 5, 6]
quicksort(vetor2, 0, len(vetor2) - 1)
print("Vetor ordenado (Teste 2):", vetor2)

# Teste 3
vetor3 = [3, -1, 2, -5, 4, -3, 2]
quicksort(vetor3, 0, len(vetor3) - 1)
print("Vetor ordenado (Teste 3):", vetor3)