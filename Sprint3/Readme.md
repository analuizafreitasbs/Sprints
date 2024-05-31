# Desadio de Python:
[Acessar:]()

Para analisar o dataset do googleplaystore.csv e gerar as visualizações necessárias, segui um roteiro detalhado utilizando as bibliotecas Pandas e Matplotlib. Primeiro, carreguei o arquivo CSV com os dados dos aplicativos e, em seguida, limpei o dataset removendo as linhas duplicadas para garantir a precisão dos resultados. Com o dataset preparado, passei a realizar as análises específicas solicitadas. Todo esse processo aconteceu no Jupyter Notebook, onde primeiro criei um ambiente virtual no VS Code para executar os comandos.

Para começar, criei um gráfico de barras identificando os cinco aplicativos com o maior número de instalações. Isso envolveu ordenar os dados pelo número de instalações e selecionar os cinco primeiros, gerando uma visualização que destaca esses aplicativos mais populares.

Depois, gerei um gráfico de pizza para mostrar a distribuição das categorias de aplicativos. Calculei a frequência de cada categoria e utilizei esses dados para criar um gráfico que representa visualmente como as categorias estão distribuídas no dataset.

Em seguida, identifiquei o aplicativo mais caro no dataset. Para isso, busquei o aplicativo com o maior preço e exibi seu nome e valor. Também determinei o número total de aplicativos classificados como 'Mature 17+' ao filtrar o dataset e contar essas entradas específicas.

Para aprofundar a análise, listei os dez aplicativos com o maior número de reviews. Ordenei o dataset por reviews e selecionei os dez principais, apresentando uma lista clara desses aplicativos e seus respectivos números de reviews.

Além disso, realizei cálculos adicionais sobre o dataset. Identifiquei os dez aplicativos com menos reviews, criando uma lista ordenada desses aplicativos. Também encontrei quantos aplicativos tinham classificação 'Everyone'.

Finalmente, para visualizar melhor os dados e tendências, criei dois tipos de gráficos adicionais: um gráfico de linha para mostrar a quantidade de apps com classificação 'Everyone' em relação às outras categorias, e outro gráfico de dispersão com os apps que têm menos reviews.

Durante todo o processo, conferi manualmente o arquivo CSV no Excel para verificar se os resultados estavam corretos. Nesse processo, percebi erros de formatação na tabela e questões redundantes, como a exibição dos 5 aplicativos mais instalados, onde muitos tinham mais de 1.000.000.000 de downloads, ou a presença de aplicativos com nomes repetidos. Fui corrigindo esses problemas com os códigos e, aparentemente, deu tudo certo.
