# Desafio da sprint 5: 

[Acessar:](https://github.com/analuizafreitasbs/Sprints/tree/main/Sprint5/Desafio)

Para o desafio, selecionei um arquivo CSV exclusivo disponível no portal de dados públicos do Governo Brasileiro e o analisei localmente em um editor de texto, garantindo sua adequação ao formato UTF-8. Após isso, carreguei o arquivo CSV 'afastrem-082017-utf8x.csv' para o bucket 'desafio.sprint5' no AWS S3. O processo inicial enfrentou desafios técnicos significativos, como erros de token e ajustes no código para atender aos requisitos específicos de busca e manipulação de dados.

Para cumprir os requisitos do desafio, desenvolvi consultas utilizando S3 Select e Python com a biblioteca Boto3. Implementei consultas individuais devido a diversas dificuldades encontradas, que demandaram tempo significativo para resolução. As consultas realizadas incluíram:

- Uma cláusula que filtrava dados com pelo menos dois operadores lógicos, utilizando AND e OR.
- Duas funções de agregação para calcular sumários estatísticos importantes nos dados, utilizando SUM e AVG.
- Uma função condicional para categorizar valores com base em critérios específicos.
- Conversões de tipos de dados para float, realizadas nas consultas 4.2 e 4.3.
- Manipulação de dados de data e strings, como formatar datas de forma legível e contar caracteres em strings.

Esse processo combinou habilidades de análise de dados, conhecimento técnico em AWS S3 e programação em Python, não consegui realizar para garantir 100%  da nota, mas fiz o que era possível para conseguir entregar e fazer todas querys.

Outro ponto importante é que tirei as chaves da AWS do arquivo commitado para manter a segurança da conta.