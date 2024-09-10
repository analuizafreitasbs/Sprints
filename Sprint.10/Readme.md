# Desafio final - Drama e romance: 

O desafio proposto tem como objetivo a construção de um Data Lake voltado para o armazenamento, processamento e análise de dados relacionados a filmes e séries, utilizando as ferramentas e conceitos fundamentais de Engenharia de Dados aprendidos durante o estágio, como Python, Docker, e diversos serviços da AWS, como S3, Glue e Athena. O foco é desenvolver um pipeline completo que envolva diferentes camadas de processamento, com o objetivo de criar um ambiente robusto para análise de dados de filmes e séries, em especial, dos gêneros de drama e romance.

### Etapa 1: Ingestão de Dados Brutos (Raw Zone)

A primeira etapa do projeto consistiu na ingestão de arquivos CSV contendo dados brutos sobre filmes e séries, como informações de títulos, anos de lançamento, gêneros, notas, número de votos, entre outros atributos essenciais para análise. Esses arquivos são inicialmente armazenados na camada **Raw** do S3, dentro do bucket `data-lake-da-ana`. Esses dados incluiram dois arquivos principais, `movies.csv` e `series.csv`, que contêm dados não tratados e precisaram ser processados e padronizados para uso posterior.

Além disso, dados complementares foram obtidos a partir da API do TMDB, utilizando a biblioteca `tmdbv3api`, com os dados agrupados em arquivos JSON de acordo com categorias específicas, como os filmes e séries de drama e romance mais bem avaliados e os com as piores avaliações. Esses dados enriqueceram o conjunto de informações e são armazenados na camada **Raw**.

### Etapa 2: Processamento e Padronização (Trusted Zone)

Na segunda etapa, os dados da camada **Raw** foram processados e transformados para garantir uma padronização e organização apropriada. Utilizando o AWS Glue e o Apache Spark, as informações dos arquivos CSV e JSON são filtradas e transformadas de acordo com regras específicas, como a remoção de duplicatas e a padronização de nomes e outros atributos. Os dados foram convertidos para o formato **Parquet**, mais eficiente para análise, e armazenados no bucket na camada **Trusted**.

Essas transformações também são refletidas no AWS Glue Data Catalog, onde as tabelas resultantes são catalogadas e prontas para uso em análises futuras, utilizando o serviço Athena da AWS.

### Etapa 3: Modelagem Dimensional (Refined Zone)

Uma vez que os dados tenham sido padronizados e organizados na camada **Trusted**, a próxima fase envolveu a criação de um modelo dimensional de dados que será utilizado para guiar o processamento final. Este modelo segue os princípios de modelagem dimensional, com o objetivo de facilitar consultas analíticas e a visualização dos dados em ferramentas como o AWS QuickSight.

Nesse processo, os dados são novamente transformados e transferidos para a camada **Refined** do Data Lake, onde serão armazenados em formato **Parquet** e particionados conforme as necessidades analíticas. Essa camada finalizou a preparação dos dados para a construção de dashboards e análises avançadas.

### Etapa 4: Consumo de Dados e Análise

A etapa final envolveu o consumo dos dados armazenados na camada **Refined** para realizar análises exploratórias e responder a perguntas específicas sobre os gêneros de drama e romance, que são o foco deste desafio. No meu caso, as questões definidas para análise são:

1. **"Em quais anos foram lançados os filmes de drama com nota superior a 8 e mais de 1.000.000 votos?"**
   - A resposta a essa pergunta envolve a filtragem dos dados de filmes de drama, focando em títulos que obtiveram uma nota média superior a 8 e que receberam mais de 1 milhão de votos. Esses filmes serão analisados para identificar o ano de lançamento, fornecendo insights sobre quais períodos foram marcantes para a produção de filmes de drama de alta qualidade.

2. **"Quais séries de drama receberam nota acima de 8.5 e qual é a mais bem votada nos últimos 20 anos?"**
   - A segunda pergunta foca nas séries de drama lançadas nos últimos 20 anos, com ênfase em títulos que receberam uma nota acima de 8.5. Além disso, a série mais bem votada desse período também será identificada, destacando tendências e preferências dos espectadores ao longo do tempo.

Essas perguntas guiaram a exploração dos dados e a elaboração de **dashboards analíticos** utilizando o AWS QuickSight, permitindo uma visualização clara e objetiva das informações extraídas do Data Lake.

### Considerações Finais

Além dos aspectos técnicos, o desafio promoveu uma análise crítica dos dados, permitindo não apenas a compreensão técnica das ferramentas de Engenharia de Dados, mas também a aplicação prática em cenários reais de análise de filmes e séries. 