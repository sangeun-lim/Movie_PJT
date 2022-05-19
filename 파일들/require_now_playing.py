
## 영화데이터

# 데이터를 받아 json 파일에 저장하는 코드 ( ? )

import requests
import json
import os

TMDB_API_KEY = str(os.getenv('TMDB_API_KEY'))

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 51):
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key=6217d09f5c6803ba98b2b2c5e261803e&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movie_nowplaying_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()
