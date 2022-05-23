from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review
from movies.models import Movie, Genre

class MypageSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class GenreSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Genre
                fields = ('genre_name',)

        genres = GenreSerializer(many=True, read_only=True)
        
        class Meta: 
            model = Movie
            fields = ('movie_id', 'title', 'released_date', 'vote_avg', 'poster_path', 'genres',)
    
    like_movies = MovieSerializer(many=True)

    class GenreSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = ('pk', 'genre_name',)

    like_genres = GenreSerializer(many=True)

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'title')
    
    reviews = ReviewSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username','like_movies', 'like_genres', 'reviews',)