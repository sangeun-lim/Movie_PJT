from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Comment, Genre
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.comment import CommentSerializer
from .serializers.genre import GenreListSerializer


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# urlpatterns = [
#     # movies
#     path('', views.movie_list),
#     path('<int:movie_id>/', views.movie_detail),
#     path('<int:movie_id>/like/', views.like_movie),
#     # comments
#     path('<int:movie_id>/comments', views.create_comment),
#     path('<int:movie_id>/comments/<int:comment_pk>/', views.comment_update_or_delete)
# ]