# Desafio da sprint 4: 

![docker](https://www.docker.com/wp-content/uploads/2021/09/Moby-Group-4-1110x747.jpeg){:height="200px" width="300px"}

### Etapa 1
Inicialmente, eu construí uma imagem Docker usando um Dockerfile que continha as instruções para criar um ambiente específico. Após construir a imagem, executei um container a partir dela para testar e validar o ambiente configurado. Utilizei o carguru.py, que exibia um carro diferente a cada execução.

### Etapa 2
Já na Etapa 2, explorei como reutilizar containers no Docker. Mostrei como reiniciar um container parado usando o comando docker start <container-id>, mantendo assim seu estado anterior e configurações para continuar as operações.

### Etapa 3
E na Etapa 3, criei um container interativo que permitia receber inputs durante sua execução. Desenvolvi um script Python que:

- Solicitava uma string via input do usuário.
- Calculava o hash SHA-1 dessa string.
- Exibia o hash utilizando o método hexdigest.
- Permitia retornar ao passo 1 para gerar novos hashes continuamente.

_E para finalizar o desafio:_ 

- Criei uma imagem Docker chamada mascarar-dados que executava o script Python desenvolvido.
- Iniciei um container a partir da imagem mascarar-dados, enviando algumas palavras para serem processadas e mascaradas.
- Documentei o script Python, o Dockerfile usado para criar a imagem mascarar-dados e o comando de inicialização do container, demonstrando como configurei e executei o ambiente Docker para o desafio proposto.
