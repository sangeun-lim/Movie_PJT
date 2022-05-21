
## 영화데이터

# 데이터를 받아 json 파일에 저장하는 코드 ( ? )

import requests
import json
import os

TMDB_API_KEY = str(os.getenv('TMDB_API_KEY'))

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 480개)
    for i in range(1, 25):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=6217d09f5c6803ba98b2b2c5e261803e&language=ko-KR&page={i}"
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

                credits_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key=6217d09f5c6803ba98b2b2c5e261803e&language=ko-KR"
                credits = requests.get(credits_url).json()

                cast_list = []
                for credit in credits['cast']:
                    if len(cast_list) < 6:
                        credit_data = {
                            'name': credit['name'],
                            'character': credit['character'],
                            'profile_path': credit['profile_path']
                        }
                        cast_list.append(credit_data)
                    
                        fields['actors'] = cast_list

                total_data.append(data)

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()
