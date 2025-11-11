# Dicionário para armazenar variáveis
variaveis = {}

def interpretar_linha(linha):
    if linha.startswith("PRINT "):
        conteudo = linha[6:].strip()
        if conteudo.startswith('"') and conteudo.endswith('"'):
            # Imprime texto literal
            print(conteudo.strip('"'))
        elif conteudo in variaveis:
            # Imprime valor da variável
            print(variaveis[conteudo])
        else:
            print(f"Variável '{conteudo}' não definida.")
    
    elif linha.startswith("SET "):
        partes = linha[4:].split("=", 1)
        if len(partes) == 2:
            nome = partes[0].strip()
            valor = partes[1].strip().strip('"')
            variaveis[nome] = valor
        else:
            print("Erro de sintaxe no comando SET.")
    
    else:
        print(f"Comando desconhecido: {linha}")

def executar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            interpretar_linha(linha.strip())

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python compilador.py programa.txt")
    else:
        executar_arquivo(sys.argv[1])
