from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Genre, Movie


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'overview', 'released_date', 'vote_avg',)


class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('genre_name',)

    genres = GenreSerializer(many=True, read_only=True)

    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

User = get_user_model()
# 추천알고리즘쓸때 필요하려나요? 혹시몰라서 아직 ..ㅎㅎ
# class MovieRecommendSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username', )
    
#     user = UserSerializer(read_only=True)