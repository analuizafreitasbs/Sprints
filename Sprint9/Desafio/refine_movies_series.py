# FIZ DE FILMES E SÉRIES EM UM CODIGO SÓ, NO CASO UM JOB APENAS
# OS DADOS QUE USEI ERAM DOS ARQUIVOS CSV, BASICAMENTE FAZ A LEITURA DAS TABELAS E FILTRA SÓ AS COLUNAS QUE VOU USAR 
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Inicializa o job
job = Job(glueContext)
job.init("process_and_refine_data", args={})

# Lendo dados das tabelas da sprint anterior
movies_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="desafiofinal",
    table_name="movies",
    transformation_ctx="movies_dynamic_frame"
)

series_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="desafiofinal",
    table_name="series",
    transformation_ctx="series_dynamic_frame"
)

# Convertendo DynamicFrames para DataFrames
movies_df = movies_dynamic_frame.toDF()
series_df = series_dynamic_frame.toDF()


# Filtrar campos relevantes pra mim dos FILMES
movies_refined = movies_df.select(
    'id', 'titulopincipal', 'titulooriginal', 'anolancamento', 'genero', 'notamedia', 'numerovotos'
)

# Filtrar campos relevantes pra mim das SERIES
series_refined = series_df.select(
    'id', 'titulopincipal', 'titulooriginal', 'anolancamento', 'genero', 'notamedia', 'numerovotos'
)

# Gravar os dados refinados em Parquet na Refined Zone dentro do meu bucket
movies_refined.write.mode('overwrite').parquet("s3://data-lake-da-ana/RefinedZone/filmes/")
series_refined.write.mode('overwrite').parquet("s3://data-lake-da-ana/RefinedZone/series/")

job.commit()