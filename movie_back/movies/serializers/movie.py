from rest_framework import serializers

from ..models import Genre, Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'overview', 'released_date', 'vote_avg',)


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