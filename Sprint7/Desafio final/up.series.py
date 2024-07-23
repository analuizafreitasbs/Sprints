import json
import boto3
from tmdbv3api import TMDb
from tmdbv3api import TV
from datetime import datetime

s3 = boto3.client('s3', # Parte das credenciais 
                  aws_access_key_id='', 
                  aws_secret_access_key='',
                  aws_session_token='')
bucket_name = 'data-lake-da-ana'

tmdb = TMDb()
tmdb.api_key = ''
tv = TV()

def lambda_handler(event, context):
    # Obtém as séries mais bem avaliadas 
    top_rated_series = tv.top_rated()

    filtered_series = []
    for s in top_rated_series:
        if 18 in s.genre_ids or 10749 in s.genre_ids: #Filtra só drama e romance
            series_data = {
                'id': s.id,
                'name': s.name,
                'first_air_date': s.first_air_date if s.first_air_date else '',
                'vote_average': s.vote_average,
                'overview': s.overview,
                'popularity': s.popularity,
                'original_language': s.original_language,
                'genre_ids': s.genre_ids if s.genre_ids else [],
          
            }
            filtered_series.append(series_data)


    data = json.dumps(filtered_series, default=str) 
   
    current_date = datetime.now().strftime('%Y/%m/%d')
    file_key = f'raw/TMDB/JSON/series/{current_date}/top_rated_drama_romance_series.json'

    # Faz o envio para o bucket
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=data, ContentType='application/json')

    return {
        'statusCode': 200,
        'body': json.dumps('Séries mais bem avaliadas de drama e romance do TMDB foram enviadas com sucesso para o S3!')
    }