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
            fields = ('genre_name')

    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'