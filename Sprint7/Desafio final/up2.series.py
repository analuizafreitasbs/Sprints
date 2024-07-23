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

def get_tv_series_by_page(page_number):
    return tv.popular(page=page_number)

def lambda_handler(event, context):
    all_series = []
    num_pages = 5  

    for page in range(1, num_pages + 1):
        print(f"Fetching page {page}...")
        series = get_tv_series_by_page(page)
        for s in series:
            if 18 in s.genre_ids or 10749 in s.genre_ids:  # Filtra só drama e romance
                series_data = {
                    'id': s.id,
                    'name': s.name,
                    'first_air_date': s.first_air_date if s.first_air_date else '',
                    'vote_average': s.vote_average,
                    'popularity': s.popularity,
                    'overview': s.overview,
                    'original_language': s.original_language,
                    'genre_ids': s.genre_ids if s.genre_ids else [],
                }
                all_series.append(series_data)

    
    sorted_series = sorted(all_series, key=lambda x: x['vote_average'])

    # Seleciona as piores avaliadas 
    worst_rated_series = sorted_series[:50]

    data = json.dumps(worst_rated_series, default=str)

    current_date = datetime.now().strftime('%Y/%m/%d')
    file_key = f'raw/TMDB/JSON/series/{current_date}/piores_drama_romance_series.json'
    
    # Envia o JSON para o S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=data, ContentType='application/json')

    return {
        'statusCode': 200,
        'body': json.dumps('Séries de drama e romance com as piores avaliações foram enviadas com sucesso para o S3!')
    }