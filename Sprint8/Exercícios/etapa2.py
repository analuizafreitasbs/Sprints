animals = [
    "cachorro", "gato", "elefante", "leão", "tigre", 
    "zebra", "girafa", "hipopótamo", "rinoceronte", "urso", 
    "canguru", "panda", "gorila", "macaco", "onça", 
    "leopardo", "lobo", "raposa", "tartaruga", "coelho"
]

animals.sort()

# Iterar sobre os itens e imprimir um a um
[print(animal) for animal in animals]

with open('animais.csv', 'w') as file:
    for animal in animals:
        file.write(f"{animal}\n")
