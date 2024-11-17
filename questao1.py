import os


def listar_conteudo_diretorio(diretorio, nivel=0):
    try:

        itens = os.listdir(diretorio)
        for item in itens:
            caminho_completo = os.path.join(diretorio, item)

            if os.path.isdir(caminho_completo):
                print("  " * nivel + f"[DIRETÓRIO] {item}/")
                listar_conteudo_diretorio(caminho_completo, nivel + 1)
            else:
                print("  " * nivel + f"[ARQUIVO] {item}")
    except PermissionError:
        print("  " * nivel + f"[PERMISSÃO NEGADA] {diretorio}")


caminho_inicial = "C:\\Program Files"
listar_conteudo_diretorio(caminho_inicial)
