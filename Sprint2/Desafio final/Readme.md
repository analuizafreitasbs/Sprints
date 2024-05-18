# Desafio Sprint2: 

## 1. Normalização dos Dados 

[Acessar:](https://github.com/analuizafreitasbs/Sprints/blob/main/Sprint2/Desafio%20final/Cmodelofisico_relacional.sql)

Objetivo: Dividir uma tabela grande e não normalizada em tabelas menores e eliminar a redundância.

*Passo 1:* Criar as tabelas normalizadas. Criei essas tabelas com o CREATE TABLE. Escolhi criar sete tabelas: cliente, carro, combustivel, locação, diaria, entrega e vendedor, usando as chaves primárias e chaves estrangeiras para unir as tabelas no diagrama.

*Passo 2:* Inserir os dados nas tabelas normalizadas. Fui inserindo os dados que encaixavam com as tabelas criadas com INSERT INTO e SELECT DISTINCT. Assim, as tabelas estão normalizadas e com dados inseridos.


## 2. Modelagem Dimensional

[Acessar:](https://github.com/analuizafreitasbs/Sprints/blob/main/Sprint2/Desafio%20final/Cmodelofisico_dimensional.sql)

Objetivo: Criar um modelo dimensional para otimizar consultas analíticas, usando fatos e dimensões.

*Passo 1:*
Criar as views para as dimensões e fatos. Criei três dimensões: dim_carro, dim_cliente e dim_tempo, além de uma view de fatos_vendas. Usei o CREATE VIEW e foi necessário usar alguns JOINs também. Os diagramas das views não ficam ligados como os diagramas das tabelas relacionais; pelo menos eu não consegui fazer isso. Além disso, no vídeo de explicação do desafio, foi mencionado que a entrega deveria ser feita de forma física.

Esses passos proporcionam uma transformação completa de um modelo de dados não normalizado para um modelo dimensional otimizado, permitindo consultas analíticas eficientes. 