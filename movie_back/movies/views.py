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


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# urlpatterns = [
#     # movies
#     path('', views.movie_list),
#     path('<int:movie_id>/', views.movie_detail),
#     path('<int:movie_id>/like/', views.like_movie),
#     # comments
#     path('<int:movie_id>/comments', views.create_comment),
#     path('<int:movie_id>/comments/<int:comment_pk>/', views.comment_update_or_delete)
# ]

# "key": "fec41ce1d899173cdc620bda18ad640bb1ca96f5"