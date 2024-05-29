import csv

atores_receita = []

with open('actors.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    
    for row in reader:
        
        if row['Total Gross']:
           
            total_gross = float(row['Total Gross'])
            ator = row['Actor']
           
            atores_receita.append((ator, total_gross))


atores_receita_ordenados = sorted(atores_receita, key=lambda x: -x[1]) #Essa parte coloca na ordem decrescente, mesma coisa do 4


with open('etapa_5.txt', mode='w') as output_file:
    for ator, total_gross in atores_receita_ordenados:
        output_file.write(f"{ator} - ${total_gross:.2f}\n")
