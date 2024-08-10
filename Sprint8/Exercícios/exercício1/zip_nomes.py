import zipfile
import os

# O arquivo foi compactado, pois era muito grande para conseguir commitar e eu conseguir usar na minha VM
nome_arquivo = 'nomes_aleatorios.txt'

nome_arquivo_zip = 'nomes_aleatorios.zip'

if os.path.exists(nome_arquivo):
    with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_arquivo)
