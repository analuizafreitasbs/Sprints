import csv

with open('actors.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    maior_numero_filmes = 0
    ator_maior_numero_filmes = None
    
    for row in reader:
        numero_filmes = int(row['Number of Movies'])
        

        if numero_filmes > maior_numero_filmes:
            maior_numero_filmes = numero_filmes
            ator_maior_numero_filmes = row['Actor']

with open('etapa_1.txt', mode='w') as output_file:

    output_file.write(f"O ator com o maior número de filmes é: {ator_maior_numero_filmes} e ele tem um total de {maior_numero_filmes} filmes.")

    
with open('etapa_1.txt', mode='r') as check_file:
    print("Conteúdo do arquivo 'etapa_1.txt':")
    print(check_file.read())


