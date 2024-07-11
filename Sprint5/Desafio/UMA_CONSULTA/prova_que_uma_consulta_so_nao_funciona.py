# NÃO FUNCIONA
import boto3

bucket_name = 'desafio.sprint5'
file_name = 'afastrem-082017-utf8x.csv'
region_name = 'us-east-1'
aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''

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
            InputSerialization={
                'CSV': {
                    'FileHeaderInfo': 'USE',
                    'RecordDelimiter': '\n',
                    'FieldDelimiter': ';',
                    'QuoteCharacter': '"'
                }
            },
            OutputSerialization={'CSV': {}},
        )

        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                print(records)

    except Exception as e:
        print(f"Erro ao executar a consulta S3 Select: {e}")

# Consulta combinada
query_combined = """
SELECT * 
FROM S3Object
WHERE (NOCARGOEMPREGO = 'AGENTE ADMINISTRATIVO' AND NOORGAO = 'MINISTDA AGRICULTURA,PECUARIA E ABAST') OR UFUPAG = 'DF'
LIMIT 10;

SELECT SUM(CAST(ANOMESREFAFAST AS FLOAT)) AS soma_rendimentos,
       AVG(CAST(ANOMESREFAFAST AS FLOAT)) AS media_rendimentos
FROM S3Object;

SELECT CASE WHEN CAST(VARENDIMENTOLIQUIDO AS FLOAT) > 5000 THEN 'ALTO' ELSE 'BAIXO' END AS categoria_rendimento
FROM S3Object
LIMIT 10;

SELECT SUBSTRING(ANOMESREFAFAST, 1, 4) AS ano,
       SUBSTRING(ANOMESREFAFAST, 5, 2) AS mes
FROM S3Object
LIMIT 10;

SELECT CHAR_LENGTH(NOSERVIDOR) AS tamanho_do_nome
FROM S3Object
LIMIT 10;
"""

print("Executando consulta combinada:")
execute_s3_select(query_combined)

