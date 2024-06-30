def recode_file_to_utf8(input_file, output_file, input_encoding='latin1'):
    try:

        with open(input_file, 'r', encoding=input_encoding) as infile:
            content = infile.read()
        
        # Escrever o arquivo com codificação UTF-8
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
        print(f"Arquivo recodificado para UTF-8 e salvo em {output_file}.")
    except Exception as e:
        print(f"Erro ao recodificar o arquivo: {e}")

input_file = 'afastrem.csv'
output_file = 'afastrem-082017-utf8x.csv'

recode_file_to_utf8(input_file, output_file)
