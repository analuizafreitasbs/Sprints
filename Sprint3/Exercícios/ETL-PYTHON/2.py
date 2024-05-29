import csv

soma = 0
contador = 0


with open('actors.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
   
    for row in reader:
        
        if row['Gross']:
            
            soma += float(row['Gross'])
            contador += 1

media = soma / contador if contador != 0 else 0
media_arredondada = round(media, 3)

with open('etapa_2.txt', mode='w') as output_file:

    output_file.write(f"A média da receita de bibleteria é: {media_arredondada}")

    
with open('etapa_2.txt', mode='r') as check_file:
    print("Conteúdo do arquivo 'etapa_2.txt':")
    print(check_file.read())



