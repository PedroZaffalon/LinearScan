import click
import os
import shutil
import json
from subdir import percorrer_subdiretorios, search_dir, allocateFile

@click.command()
@click.option('--path', '-p', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output file/directory.')
@click.option('--individual', '-i', is_flag=True, help='Generate one output file for each input file')
@click.option('--registers', '-r', default=8, help='Number of registers.')
@click.option('--fitness', '-f', is_flag=True, help='Display metric in results (f = 1 - spillCost/totalSpillCost).')
@click.option('--subdirectorys', '-s', is_flag=True, default=False, help='Iterate all subdirectories and search for .ll files.')
@click.option('--clear', '-c', is_flag=True, default=False, help='Remove files in output directory.')
@click.option('--singlegraph', '-g', is_flag=True, default=False, help='Only a single graph each file.')

def cli(path, output, individual, registers, fitness, subdirectorys, clear, singlegraph):
    if path == "":
        path = os.getcwd()

    if output == "":
        if individual:
            output = os.getcwd()
        else: 
           output = "log.json"
        clear = False
    else:
        if individual:
            output_dir = output
        else:
            if os.path.isdir(output):
                output_dir = output
                output = os.path.join(output, "log.json")
            else:
                output_dir = os.path.dirname(output)
        if not os.path.exists(output_dir): 
            try:
                # Criar o diretório se não existir
                os.makedirs(output_dir)
            except OSError as e:
                print(f"Erro ao criar o diretório '{output_dir}': {e}")

    if clear:
        if os.path.exists(output):
        # Percorre todos os arquivos e pastas dentro do diretório
            for item in os.listdir(output):
                item_path = os.path.join(output, item)

                # Verifica se é um arquivo
                if os.path.isfile(item_path):
                    os.remove(item_path)
                # Verifica se é uma pasta
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

    
    # Verificar se o diretório existe
        
    if os.path.isfile(path) and path.endswith(".json"):
        result = allocateFile(path, registers, singlegraph, fitness)
        if len(result) > 0:
            outputFileName = os.path.basename(path)[:-5] + "_results.json"
            outputPath = os.path.join(output, outputFileName)
            with open(outputPath, 'w') as outputFile:
                json.dump(result, outputFile, indent=4)
    else:
        results = []
        if subdirectorys:
            # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista
            subdirs = percorrer_subdiretorios(path)

            # loop para executar o comando com cada subdiretório como argumento
            for subdir in subdirs:
                print(subdir)
                results += search_dir(subdir, output, registers, singlegraph, individual, fitness)
        results += search_dir(path, output, registers, singlegraph, individual, fitness)
        if not individual:
            with open(output, 'w') as outputFile:
                json.dump(results, outputFile, indent=4)



if __name__ == '__main__':
    cli()