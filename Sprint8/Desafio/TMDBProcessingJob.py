# O script para filtrar os dados e enviar eles em parquet para nova pasta trustedzone no bucket por meio de um job
# Nesse caso é de séries, o de movies é só substituir as palavras series por movies, mas o código é o mesmo
import pyspark.sql.functions as F
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.transforms import *

# Criar o contexto Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Carregar ds dados JSON que estavam na camada raw do bucket
df_worst_rated_series_tmdb = spark.read.json("s3://data-lake-da-ana/raw/TMDB/JSON/series/2024/07/22/piores_drama_romance_series.json/")
# A DIFERENÇA PRO DE MOVIES, É QUE LÁ SE TRATA DOS MELHORES FILMES E AQUI DA PIORES SÉRIES, MAS SÓ FAZER ESSAS ALTERAÇÕES
df_series_tmdb = df_worst_rated_series_tmdb

# Realizar transformações necessárias
df_transformed_series_tmdb = df_series_tmdb.withColumn("first_air_date", F.col("first_air_date").cast("date")) \
                                           .withColumn("vote_average", F.col("vote_average").cast("double"))

# Salvar dados transformados na TrustedZone em formato Parquet
df_transformed_series_tmdb.write.mode("overwrite").parquet("s3://data-lake-da-ana/TrustedZone/2024/07/22/series_tmdb/")
# OS DADOS EM JSON PEDIAM A DATA JUNTO COM O CAMINHO,NÃO FIZ GRANDES FILTRAGENS POIS ACHO QUE NEM VOU USAR ESSE 



