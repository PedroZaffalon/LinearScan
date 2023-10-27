import json

def linearScan(input_file, registers, singlegraph):
    graphs = ler_arquivo_json(input_file)
    if singlegraph:
        graphs = {1 : graphs}
    results = {}
    return results


def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"O arquivo '{nome_arquivo}' não é um JSON válido.")
        return {}
