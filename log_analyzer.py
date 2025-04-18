import os

def ler_arquivo_log(caminho):
    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return []

    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()
    return linhas

# Teste
log = ler_arquivo_log("exemplo.log")
print("Arquivo lido com sucesso!")
print(f"{len(log)} linhas encontradas.")

def analisar_log(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            print("Arquivo lido com sucesso!")
            print(f"{len(linhas)} linhas encontradas.")

            contagem_tipos = {
                "INFO": 0,
                "ERROR": 0,
                "WARNING": 0
            }

            for linha in linhas:
                for tipo in contagem_tipos:
                    if tipo in linha:
                        contagem_tipos[tipo] += 1

            print("\nResumo por tipo de log:")
            for tipo, qtd in contagem_tipos.items():
                print(f"{tipo}: {qtd}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    analisar_log("exemplo.log")
