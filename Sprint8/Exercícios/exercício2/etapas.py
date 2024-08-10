# SCRIPT QUE USEI NO SPARK NO LINUX PARA FILTRAR OS DADOS DOS ARQ QUE EU CRIEI
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, rand

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("NomeAleatoriosApp") \
    .getOrCreate()

# Define o caminho para o arquivo de texto
file_path = ".../nomes_aleatorios.txt" # tava no linux então é outro caminho

df_nomes = spark.read.csv(file_path, header=False, inferSchema=True)

# Pede parar renomear a coluna nomes
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")

# Mostra o esquema do DataFrame
df_nomes.printSchema()

# Mostra 10 linhas do DataFrame
df_nomes.show(10)

# Importa a função para adicionar a coluna com valor aleatório
from pyspark.sql.functions import expr

# Valores possíveis para a coluna Escolaridade
valores_escolaridade = ["Fundamental", "Medio", "Superior"]

# Adiciona a coluna Escolaridade com valor aleatório
df_nomes = df_nomes.withColumn("Escolaridade", expr(f"CASE WHEN rand() < 1/3 THEN '{valores_escolaridade[0]}' " \
                                                      f"WHEN rand() < 2/3 THEN '{valores_escolaridade[1]}' " \
                                                      f"ELSE '{valores_escolaridade[2]}' END"))

# Países da América do Sul
paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", 
          "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]

# Adiciona a coluna Pais com valor aleatório
df_nomes = df_nomes.withColumn("Pais", expr(f"CASE WHEN rand() < 1/13 THEN '{paises[0]}' "
                                            f"WHEN rand() < 2/13 THEN '{paises[1]}' "
                                            f"WHEN rand() < 3/13 THEN '{paises[2]}' "
                                            f"WHEN rand() < 4/13 THEN '{paises[3]}' "
                                            f"WHEN rand() < 5/13 THEN '{paises[4]}' "
                                            f"WHEN rand() < 6/13 THEN '{paises[5]}' "
                                            f"WHEN rand() < 7/13 THEN '{paises[6]}' "
                                            f"WHEN rand() < 8/13 THEN '{paises[7]}' "
                                            f"WHEN rand() < 9/13 THEN '{paises[8]}' "
                                            f"WHEN rand() < 10/13 THEN '{paises[9]}' "
                                            f"WHEN rand() < 11/13 THEN '{paises[10]}' "
                                            f"WHEN rand() < 12/13 THEN '{paises[11]}' "
                                            f"ELSE '{paises[12]}' END"))

# Adiciona a coluna AnoNascimento com valor aleatório entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (1945 + (rand() * (2010 - 1945)).cast("int")))

# Filtra as pessoas nascidas neste século (2001 - 2100)
df_select = df_nomes.filter(col("AnoNascimento") >= 2001)

# Cria uma tabela temporária para usar Spark SQL
df_nomes.createOrReplaceTempView("pessoas")

df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2001")

# Conta o número de pessoas nascidas entre 1980 e 1994
count_millennials = df_nomes.filter(col("AnoNascimento").between(1980, 1994)).count()

print(f"Número de Millennials: {count_millennials}")

# Executa a consulta SQL para contar pessoas da geração Millennials
count_millennials_sql = spark.sql("SELECT COUNT(*) AS num_millennials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")

count_millennials_sql.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa a Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("NomeAleatoriosApp") \
    .getOrCreate()

# Cria uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Baby Boomers (1944-1964)
baby_boomers_query = """
SELECT Pais, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento BETWEEN 1944 AND 1964
GROUP BY Pais
"""

# Geração X (1965-1979)
geracao_x_query = """
SELECT Pais, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento BETWEEN 1965 AND 1979
GROUP BY Pais
"""

# Millennials (1980-1994)
millennials_query = """
SELECT Pais, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento BETWEEN 1980 AND 1994
GROUP BY Pais
"""

# Geração Z (1995-2015)
geracao_z_query = """
SELECT Pais, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento BETWEEN 1995 AND 2015
GROUP BY Pais
"""
baby_boomers_df = spark.sql(baby_boomers_query)
geracao_x_df = spark.sql(geracao_x_query)
millennials_df = spark.sql(millennials_query)
geracao_z_df = spark.sql(geracao_z_query)

# Mostra os resultados para cada geração
print("Baby Boomers:")
baby_boomers_df.show()

print("Geração X:")
geracao_x_df.show()

print("Millennials:")
millennials_df.show()

print("Geração Z:")
geracao_z_df.show()

# Salva os resultados em arquivos CSV
baby_boomers_df.write.csv('baby_boomers.csv', header=True)
geracao_x_df.write.csv('geracao_x.csv', header=True)
millennials_df.write.csv('millennials.csv', header=True)
geracao_z_df.write.csv('geracao_z.csv', header=True)
