import csv
from collections import Counter


contador_filmes = Counter()


with open('actors.csv', mode='r') as file:
    reader = csv.DictReader(file)
    

    for row in reader:
      
        if row['#1 Movie']:
         
            contador_filmes[row['#1 Movie']] += 1


filmes_ordenados = sorted(contador_filmes.items(), key=lambda x: (-x[1], x[0]))


with open('etapa_4.txt', mode='w') as output_file:
    for filme, quantidade in filmes_ordenados:
        output_file.write(f"O filme '{filme}' aparece {quantidade} vez(es) no dataset.\n")
