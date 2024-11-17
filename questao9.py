class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percurso_em_ordem(nodo):
    if nodo is None:
        return []
    return percurso_em_ordem(nodo.esquerda) + [nodo.valor] + percurso_em_ordem(nodo.direita)

def inserir_na_bst(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir_na_bst(raiz.esquerda, valor)
    else:
        raiz.direita = inserir_na_bst(raiz.direita, valor)
    return raiz

def gerar_arvore_de_bst(arr):
    raiz = None
    for valor in arr:
        raiz = inserir_na_bst(raiz, valor)
    return raiz

if __name__ == "__main__":
    valores = [3,456,2,89,546,678433,3,87,2,1,8964,4,867,23,87]
    raiz = gerar_arvore_de_bst(valores)
    resultado = percurso_em_ordem(raiz)
    print(resultado)
