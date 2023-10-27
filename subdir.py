import os
import json
from linearScan import linearScan

# função para percorrer recursivamente todos os subdiretórios da pasta raiz e salvar os caminhos em uma lista
def percorrer_subdiretorios(root_dir):
    # lista para armazenar os caminhos dos subdiretórios
    subdirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # para cada subdiretório encontrado, adicione o caminho à lista
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdirs.append(subdir_path)
    return subdirs

def search_dir(dir, output, registers, singlegraph):
    results = []
    for file_name in os.listdir(dir):
        if file_name.endswith(".json"):
            input_file_name = os.path.join(dir, file_name)
            result = linearScan(input_file_name, registers, singlegraph)
            if result is not None:
                results.append(result)
    with open(output, 'w') as outputFile:
        json.dump(results, outputFile, indent=4)
            