import json
import boto3
from tmdbv3api import TMDb
from tmdbv3api import Movie
from datetime import datetime

s3 = boto3.client('s3', # Parte das credenciais 
                  aws_access_key_id='', 
                  aws_secret_access_key='',
                  aws_session_token='')
bucket_name = 'data-lake-da-ana'

tmdb = TMDb()
tmdb.api_key = ''
movie = Movie()

def get_movies_by_page(page_number):
    return movie.popular(page=page_number)

def lambda_handler(event, context):
    all_movies = []
    num_pages = 5

    for page in range(1, num_pages + 1):
        print(f"Fetching page {page}...")
        movies = get_movies_by_page(page)
        for m in movies:
            if 18 in m.genre_ids or 10749 in m.genre_ids:  # Filtra só drama e romance
                movie_data = {
                    'id': m.id,
                    'title': m.title,
                    'release_date': m.release_date if m.release_date else '',
                    'vote_average': m.vote_average,  
                    'popularity': m.popularity,
                    'overview': m.overview,
                    'original_language': m.original_language,
                    'genre_ids': m.genre_ids if m.genre_ids else [],
                }
                all_movies.append(movie_data)

    sorted_movies = sorted(all_movies, key=lambda x: x['vote_average'])

    # Seleciona os piores avaliados 
    worst_rated_movies = sorted_movies[:50]

    data = json.dumps(worst_rated_movies, default=str)

    current_date = datetime.now().strftime('%Y/%m/%d')
    file_key = f'raw/TMDB/JSON/movies/{current_date}/piores_drama_romance_movies.json'
    
    # Envia o JSON para o S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=data, ContentType='application/json')

    return {
        'statusCode': 200,
        'body': json.dumps('Filmes de drama e romance com as piores avaliações foram enviados com sucesso para o S3!')
    }