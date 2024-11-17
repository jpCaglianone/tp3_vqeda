def torre_de_hanoi(n, origem, destino, auxiliar, pinos):
    if n == 1:
        disco = pinos[origem].pop()
        pinos[destino].append(disco)
        print(f"Mova o disco {disco} de {chr(65 + origem)} para {chr(65 + destino)}")
        return

    torre_de_hanoi(n - 1, origem, auxiliar, destino, pinos)

    disco = pinos[origem].pop()
    pinos[destino].append(disco)
    print(f"Mova o disco {disco} de {chr(65 + origem)} para {chr(65 + destino)}")

    torre_de_hanoi(n - 1, auxiliar, destino, origem, pinos)

def iniciar_torre_de_hanoi(n):
    pinos = [list(range(n, 0, -1)), [], []]

    print("Estado inicial dos pinos:")
    mostrar_estado_pinos(pinos)

    torre_de_hanoi(n, 0, 2, 1, pinos)

    print("\nEstado final dos pinos:")
    mostrar_estado_pinos(pinos)

def mostrar_estado_pinos(pinos):
    for i, pino in enumerate(pinos):
        print(f"Pino {chr(65 + i)}: {pino}")


iniciar_torre_de_hanoi(5)
