# Erro em executar apenas uma consulta: 

Durante minhas tentativas de executar consultas no AWS S3, enfrentei alguns desafios ao tentar combinar várias consultas em uma única expressão SQL. No início, achei que seria conveniente condensar tudo em uma única consulta para simplificar o processo e alcançar 100% da nota. No entanto, dessa maneira o código não funcionava de jeito nenhum e sempre dava erro em alguma linha, embora na linha não houvesse erro aparente.

Ao tentar criar uma consulta única que cobrisse diferentes requisitos, como filtros complexos, funções de agregação e manipulação de dados, me deparei com erros frequentes de sintaxe ou operações não suportadas, uma vez que o S3 é bastante sensível ao que pode ser usado nele, por exemplo, não aceita o GROUP BY.

Foi mais eficaz estruturar consultas separadas, cada uma focando em um aspecto específico dos dados, pois assim o código funcionava corretamente.

![erro](https://github.com/analuizafreitasbs/Sprints/blob/main/Sprint5/Desafio/UMA_CONSULTA/Captura%20de%20tela%202024-06-29%20235522.png?raw=true)