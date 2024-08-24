# Desafio final (entrega 4): 

O objetivo desta entrega do desafio final era realizar uma limpeza nos dados, refinando-os para serem usados na última etapa do projeto. No meu caso, utilizei os dados em CSV para responder às minhas perguntas, pois não vi necessidade de usar os dados do TMDB. Os arquivos em CSV já correspondiam às consultas que fiz no site do TMDB, além de serem mais simples de manusear.

A realização desta etapa do desafio foi relativamente simples. O job já estava configurado para ler ambos os tipos de arquivos, movies e series, mantendo apenas as colunas necessárias para responder às minhas perguntas, como: id, titulopincipal, titulooriginal, anolancamento, genero, notamedia, e numerovotos. O script consulta as tabelas que criei na sprint anterior, dentro do banco de dados "desafiofinal", e realiza a filtragem dessas colunas, enviando os dados filtrados para o meu bucket na pasta RefinedZone.

Depois disso, criei um crawler para gerar as duas tabelas com os arquivos já filtrados e, em seguida, fiz consultas no Athena para verificar se conseguia responder às duas perguntas propostas por mim, e também criei as viewes dessas consultas que estão disponiveis as 10 primeiras linhas na pasta de desafio. De modo geral, não encontrei grandes problemas para resolver o desafio. A única dúvida que tive foi em relação à questão do "modelo de dados da camada refined desenhado em ferramentas de modelagem". No entanto, fiz o melhor que pude para atender a essa solicitação e documentar o que considerei correto.

### Link para acessar as evidências do desafio: [Acessar:](https://github.com/analuizafreitasbs/Sprints/tree/main/Sprint9/Evid%C3%AAncias)

