# O script para filtrar os dados e enviar eles em parquet para nova pasta trustedzone no bucket por meio de um job
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame  

# Parte do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Para processar os CSVs que estavam no bucket
def process_csv(table_name, output_path):
    # Cria um DynamicFrame
    datasource0 = glueContext.create_dynamic_frame.from_catalog(
        database="desafiofinal",
        table_name=table_name,
        transformation_ctx="datasource0"
    )

    # Faz as transformações de limpeza e padronização
    applymapping1 = ApplyMapping.apply(frame=datasource0, mappings=[
        ("id", "string", "id", "string"),
        ("tituloPincipal", "string", "tituloPincipal", "string"),
        ("tituloOriginal", "string", "tituloOriginal", "string"),
        ("anoLancamento", "int", "anoLancamento", "int"),
        ("tempoMinutos", "int", "tempoMinutos", "int"),
        ("genero", "string", "genero", "string"),
        ("notaMedia", "double", "notaMedia", "double"),
        ("numeroVotos", "int", "numeroVotos", "int"),
        ("generoArtista", "string", "generoArtista", "string"),
        ("personagem", "string", "personagem", "string"),
        ("nomeArtista", "string", "nomeArtista", "string"),
        ("anoNascimento", "int", "anoNascimento", "int"),
        ("anoFalecimento", "int", "anoFalecimento", "int"),
        ("profissao", "string", "profissao", "string"),
        ("titulosMaisConhecidos", "string", "titulosMaisConhecidos", "string")
    ], transformation_ctx="applymapping1")

    resolvechoice2 = ResolveChoice.apply(frame=applymapping1, choice="make_cols", transformation_ctx="resolvechoice2")
    dropnullfields3 = DropNullFields.apply(frame=resolvechoice2, transformation_ctx="dropnullfields3")

    # Converte para DataFrame para usar o dropDuplicates
    df = dropnullfields3.toDF()

    # Remove títulos repetidos (baseado na coluna 'tituloPincipal'), essa parte tira os titúlos duplicados
    df = df.dropDuplicates(['tituloPincipal'])

    # Converte de volta para DynamicFrame
    dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

    # Grava em Parquet como foi pedido
    datasink4 = glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame,
        connection_type="s3",
        connection_options={"path": output_path},
        format="parquet",
        transformation_ctx="datasink4"
    )

# Processar os arquivos movies e series para nova pasta do bucket
process_csv("movies", "s3://data-lake-da-ana/TrustedZone/CSV/movies/")
process_csv("series", "s3://data-lake-da-ana/TrustedZone/CSV/series/")

job.commit()


