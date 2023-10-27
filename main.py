import click
import os
import shutil
from subdir import percorrer_subdiretorios, search_dir

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output file.')
@click.option('--registers', '-r', default=8, help='Number of registers.')
@click.option('--subdirectorys', '-s', is_flag=True, default=False, help='Iterate all subdirectories and search for .ll files.')
@click.option('--clear', '-c', is_flag=True, default=False, help='Remove files in output directory.')
@click.option('--singlegraph', '-g', is_flag=True, default=False, help='Only a single graph each file.')

def cli(dir, output, registers, subdirectorys, clear, singlegraph):
    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir
        clear = False

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

    if not os.path.exists(output):
        os.makedirs(output)

    output_dir = os.path.dirname(output)

    # Verificar se o diretório existe
    if not os.path.exists(output_dir):
        try:
            # Criar o diretório se não existir
            os.makedirs(output_dir)
        except OSError as e:
            print(f"Erro ao criar o diretório '{output_dir}': {e}")

    if subdirectorys:
        # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista
        subdirs = percorrer_subdiretorios(dir)

        # loop para executar o comando com cada subdiretório como argumento
        for subdir in subdirs:
            search_dir(subdir, output, registers, singlegraph)
    search_dir(dir, output, registers, singlegraph)



if __name__ == '__main__':
    cli()