import boto3

bucket_name = 'desafio.sprint5'
file_name = 'afastrem-082017-utf8x.csv'  
region_name = 'us-east-1'
aws_access_key_id = 'XXXXXXXXXXXXXXXXXXXXX'
aws_secret_access_key = 'XXXXXXXXXXXX'
aws_session_token = 'XXXXXXXXXXXXXXXXXXXXXXX'

# COMO FOI FALADO QUE SÓ IAM OLHAR A QUERY, TIREI MINHAS CHAVES DO ARQ NA HORA DE COMMITAR PARA MANTER A SEGURANÇA DA CONTA
# PORÉM NO VÍDEO E APARECE NORMALMENTE, FOI POR UMA QUESTÃO DE SEGURANÇA MESMO.
def execute_s3_select(query):
    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )
        s3_client = session.client('s3', region_name=region_name)

        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=file_name,
            Expression=query,
            ExpressionType='SQL',
            InputSerialization={'CSV': {'FileHeaderInfo': 'USE', 'RecordDelimiter': '\n', 'FieldDelimiter': ';', 'QuoteCharacter': '"'}},
            OutputSerialization={'CSV': {}},
        )

        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                print(records)

    except Exception as e:
        print(f"Erro ao executar a consulta S3 Select: {e}")


# Um cláusula que filtra dados usando pelo menos dois operadores lógicos
query_4_1 = """
    SELECT * 
    FROM S3Object
    WHERE (NOCARGOEMPREGO = 'AGENTE ADMINISTRATIVO' AND NOORGAO = 'MINISTDA AGRICULTURA,PECUARIA E ABAST') OR UFUPAG = 'DF'
    LIMIT 10;
"""
# Duas funções de Agregação 

query_4_2 = """
    SELECT SUM(CAST(ANOMESREFAFAST AS FLOAT)) AS soma_rendimentos,  
           AVG(CAST(ANOMESREFAFAST AS FLOAT)) AS media_rendimentos
    FROM S3Object;
"""
#  Uma função Condicional
query_4_3 = """
    SELECT 
         CASE 
         WHEN CAST(VARENDIMENTOLIQUIDO AS FLOAT) > 5000 THEN 'ALTO'
         ELSE 'BAIXO'
        END AS categoria_rendimento
    FROM S3Object
    LIMIT 10;  
"""
# A QUERY 4.4 NÃO EXISTE, POIS ERA DE CONVERSÃO E ESSE PROCESSO DE CONVERSÃO JÁ TÁ DENTRO DA 4.3 E NA 4.2 TRANSFORMANDO 
# OS NÚMEROS PARA FLOAT.

# Uma função de Data
query_4_5 = """
    SELECT 
        SUBSTRING(ANOMESREFAFAST, 1, 4) AS ano,
        SUBSTRING(ANOMESREFAFAST, 5, 2) AS mes
    FROM S3Object
    LIMIT 10;
"""
# Uma função de String
query_4_6 = """
    SELECT
        CHAR_LENGTH(NOSERVIDOR) AS tamanho_do_nome
    FROM S3Object
    LIMIT 10;
"""

print("Consulta 4.1:")
execute_s3_select(query_4_1)

print("\nConsulta 4.2:")
execute_s3_select(query_4_2)

print("\nConsulta 4.3:")
execute_s3_select(query_4_3)

# A QUERY 4.4 NÃO EXISTE, POIS ERA DE CONVERSÃO E ESSE PROCESSO DE CONVERSÃO JÁ TÁ DENTRO DA 4.3 E NA 4.2 TRANSFORMANDO 
# OS NÚMEROS PARA FLOAT.

print("\nConsulta 4.5:")
execute_s3_select(query_4_5)

print("\nConsulta 4.6:")
execute_s3_select(query_4_6)

