import json
import boto3
from tmdbv3api import TMDb
from tmdbv3api import Movie
from datetime import datetime

s3 = boto3.client('s3',  # Parte das credenciais 
                  aws_access_key_id='', 
                  aws_secret_access_key='',
                  aws_session_token='')
bucket_name = 'data-lake-da-ana'

tmdb = TMDb()
tmdb.api_key = '' #Parte da chave de API
movie = Movie()

def lambda_handler(event, context):
    # Obtém os filmes mais bem avaliados 
    top_rated_movies = movie.top_rated()

    filtered_movies = []
    for m in top_rated_movies:
        if 18 in m.genre_ids or 10749 in m.genre_ids:  #Filtra só drama e romance
            movie_data = {
                'id': m.id,
                'title': m.title,
                'release_date': m.release_date if m.release_date else '',
                'vote_average': m.vote_average,
                'overview': m.overview,
                'popularity': m.popularity,
                'original_language': m.original_language,
                'genre_ids': m.genre_ids if m.genre_ids else [],
               
            }
            filtered_movies.append(movie_data)


    data = json.dumps(filtered_movies, default=str) 

    current_date = datetime.now().strftime('%Y/%m/%d')
    file_key = f'raw/TMDB/JSON/movies/{current_date}/top_rated_drama_romance_movies.json'
    
    # Envia o JSON para o S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=data, ContentType='application/json')

    return {
        'statusCode': 200,
        'body': json.dumps('Filmes mais bem avaliados de drama e romance do TMDB foram enviados com sucesso para o S3!')
    }