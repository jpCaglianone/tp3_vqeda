def soma_lista_manual(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice] + soma_lista_manual(lista, indice + 1)

print(soma_lista_manual([1, 2, 3, 4]))  
