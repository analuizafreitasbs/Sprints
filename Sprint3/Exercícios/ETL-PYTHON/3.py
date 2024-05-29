import csv


maior_media_ator = None
maior_media = 0


with open('actors.csv', mode='r') as file:
    reader = csv.DictReader(file)
    

    for row in reader:
      
        if row['Average per Movie']:
        
            media_por_filme = float(row['Average per Movie'])
            
       
            if media_por_filme > maior_media:
                maior_media = media_por_filme
                maior_media_ator = row['Actor']

with open('etapa_3.txt', mode='w') as output_file:
    output_file.write(f"O ator com a maior média de receita de bilheteria bruta por filme é o {maior_media_ator} e tem uma média de ${maior_media:.3f} por filme.")

    
with open('etapa_3.txt', mode='r') as check_file:
    print("Conteúdo do arquivo 'etapa_3.txt':")
    print(check_file.read())




