import zipfile
import os

# Nome do arquivo que será compactado
nome_arquivo = 'nomes_aleatorios.txt'

nome_arquivo_zip = 'nomes_aleatorios.zip'

if os.path.exists(nome_arquivo):
    # Cria o arquivo ZIP e adiciona o arquivo de nomes nele
    with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_arquivo)

    print(f"Arquivo {nome_arquivo_zip} criado com sucesso!")
