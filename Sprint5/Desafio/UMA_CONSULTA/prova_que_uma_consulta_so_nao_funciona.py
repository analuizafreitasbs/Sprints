# NÃO FUNCIONA
import boto3

bucket_name = 'desafio.sprint5'
file_name = 'afastrem-082017-utf8x.csv'
region_name = 'us-east-1'
aws_access_key_id = 'ASIA47CRZEXO7U7BRYV7'
aws_secret_access_key = 'O9By7wx3Q/VPOPn4wWDKi03MW0T0rFUXPCGJMo8a'
aws_session_token = 'IQoJb3JpZ2luX2VjEHwaCXVzLWVhc3QtMSJHMEUCIQDoY+te6kKvjD5wdwFFtysK9ncAJzYrimJNvshUpmpKkwIgAY4Nros4hjiyto2oTnknszxC4W0aCxnrmQDo5+auHGsqnQMINRAAGgw4OTEzNzcyMzEzMjUiDApSUNU7Hp1+KnSf2Sr6AqOZ57LZNxNSLDHEsDwVcZ8ZDdsuYKiMuiw8+gIxQVhi0E1KFmScbEzTLCkLnytkjvDcMgSYQ3Pd52YN+FCGR2wD1JGntX/U6zg/9PmI2x3j7K4LJaTlYnGAlgiE7mEOVgx/I5cK2oFnDUU4fuYZIym02YwD9Vbgs0lrQLM7gIDTSUtXHAfl14BoWotxXg2MJQOX22ZactKPpGinPqFEtHqnqY2DmthWDIx6sy7jTvtsRHZwhkYUnf2oItfCT86DDRDJCu21F1m3qHeeViNHqrKMS1ZlBiCTDs0HyBn6mZBtWi5/iHBtx8Ou+N/G/aG+SfV5GqgFcO5i/x93unPpt3rega0b0JtXNPYGVjTJ8gjhAKd3FNH039OzdVUUamP3GJdb59lMZ7eqr8ekIK+0pBsN8QrOU+dBRuU+zrhSzNwmD49iYzA5bzrtzc4Hxu5ghzXSuWTu0Iqsmqa7ZYfmZjSQdByYDTe+6AsOkEEgZADX6NKBsN55Xcr9EzCew4G0BjqmAYgcNjd9/2fDPMuEZNOBKntMB/BmziuGON/0hqRDXkZkegH1ZrBXIX1/loGREorf5lx4xT1/EtW859OEay+l1LyycMR6ybi128ENYy4xgkbUjeY8o6flftQPQxDqMpUAPct1QQmxA69R1ADS/0/nvjpCg4PZ9b43kZEYTL2K+zrs6y6KsQ5taXeHY4dDPc+kQ2XIjGiG6ZMLlXeFZv4Frp2JEhRgRSs='

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

