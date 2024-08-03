# Exercícios - Sprint 7:

No primeiro exercício, eu precisava contar as palavras de um arquivo `README.md` a partir de um repositório Git, usando Docker e Spark. Como não consegui fazer isso diretamente com Docker, usei o Google Colab como alternativa. Baixei o arquivo `README.md` usando `wget` e, em seguida, utilizei bibliotecas Python no Colab para ler o arquivo, processar o texto, e contar as palavras. Os resultados mostraram a frequência das palavras no arquivo.

No segundo exercício, utilizei o AWS Glue para processar dados. Criei um job no Glue para ler o arquivo `nomes.csv` do S3 e escrevi um script PySpark para processar o arquivo. O script incluiu a leitura do arquivo, a impressão do schema, a alteração para maiúsculas, a contagem de linhas, e a análise dos dados para encontrar o nome mais frequente e o total de registros por ano. Depois, escrevi o resultado no S3 em formato JSON, particionado por `sexo` e `ano`. Segui todos os passos e obtive os resultados que aparentemente eram esperados.

P.S: Estou entregando os exercícios da Sprint 7 durante a Sprint 8 porque decidi focar no desafio e usar o tempo restante para estudar para a faculdade, já que era o final do semestre. Esse arranjo foi acordado com o monitor.

![colab]()