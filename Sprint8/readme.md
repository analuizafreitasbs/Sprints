# Desafio final (entrega 3): 

_O desafio final tinha como objetivo realizar uma filtragem nos arquivos da camada RAW que foram inseridos no bucket durante as sprints anteriores para serem inseridos na camada TrustedZone. Para começar, criei uma role no IAM para ser usada com o AWS Glue. Em seguida, configurei um crawler para os arquivos CSV, criando um novo banco de dados. Com a execução do crawler, novas tabelas foram geradas automaticamente com base nos arquivos CSV, com as colunas corretamente mapeadas. O desafio também tem a intenção de garantir que esses dados estejam em um formato unificado, para que possam ser acessados no AWS Athena utilizando SQL._

_A partir daí, desenvolvi um job no AWS Glue para cada tipo de arquivo. Escrevi scripts em Python utilizando Spark, dentro do ambiente do AWS Glue, que processavam e enviavam os arquivos filtrados para o bucket no caminho desejado, no formato Parquet. Como as perguntas que eu queria responder exigiam uma grande quantidade de dados, optei por não fazer muitas filtragens nos arquivos, priorizando garantir que todos os dados necessários estivessem disponíveis._

_Para os arquivos JSON, o processo foi similar, mas com algumas diferenças devido ao formato do arquivo, precisando fazer outro Job. Embora a exibição dos dados JSON nas tabelas não seja tão simples quanto nos arquivos CSV, subi os JSONs mais como complemento, caso fosse necessário. No entanto, acredito que minhas perguntas podem ser respondidas utilizando apenas os arquivos CSV._

_Minhas perguntas são: "Qual o ano de lançamento dos filmes mais bem avaliados de romance e drama?" e "Quais séries de drama e romance receberam nota acima de 8, e qual é a mais votada nos últimos 10 anos?". Acrescentei alguns detalhes às perguntas e excluí arquivos JSON que provavelmente não seriam utilizados. Caso precise utilizá-los no futuro, sei qual o processo necessário._

_Escolhi essas perguntas porque, ao analisar os dados, foi o que mais chamou minha atenção, além de que, pessoalmente, sou apreciadora de séries e filmes, então essas informações me ajudarão a escolher boas produções para assistir no futuro. Observei que é possível responder essas perguntas utilizando apenas os arquivos CSV, recorrendo aos JSONs apenas se necessário. Também escolhi analisar as piores séries como uma possível variante para a segunda pergunta, caso eu decida alterá-la._

_No geral, acredito que o desafio foi resolvido de maneira satisfatória, e essas perguntas foram escolhidas com base em meus interesses pessoais e na relevância dos dados no meu ponto de vista._

### Link para acessar as evidências do desafio: [Acessar:](https://github.com/analuizafreitasbs/Sprints/tree/main/Sprint8/Evid%C3%AAncias)

