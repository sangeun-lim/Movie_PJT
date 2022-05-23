from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers.genre import GenreListSerializer
from .models import Movie, Comment, Genre

from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.comment import CommentSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.db.models import Q

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_popular(request):
    movies = Movie.objects.filter(vote_avg__gte=8).distinct()[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def movie_genre(request):
    selected = request.data.get('selected')
    # keyword = request.data
    # actors.name 추가 (자꾸 오류뜸)
    movies = Movie.objects.filter(genres=selected).distinct()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    # movies = Movie.objects.all()
    # print(movies)
    # for movie in movies:
    #     print(movie)
    #     if selected in movie['genres']:
    #         serializer = MovieListSerializer(movie, many=True)
    #         return Response(serializer.data)

@api_view(['POST'])
def like_movies(request):
    like_genre_dic = request.data
    like_genre = max(like_genre_dic, key=like_genre_dic.get)
    movies = Movie.objects.filter(genres=like_genre).distinct()
    serializer = MovieSerializer(movies, many=True)
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
@permission_classes([IsAuthenticated])
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

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request, movie_id, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_id)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

@api_view(['POST'])
def search(request):
    keyword = request.data.get('keyword')
    # keyword = request.data
    # actors.name 추가 (자꾸 오류뜸)
    movies = Movie.objects.filter(
        Q(title__contains=keyword) |
        Q(overview__contains=keyword)
    ).distinct()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)