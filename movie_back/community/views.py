from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Review, Rate
# from .models import Comment
from .serializers.comment import CommentSerializer
from .serializers.review import ReviewSerializer
from .serializers.rate import RateSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# 영화 리뷰 조회 및 리뷰 생성(댓글 개념?)
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def review_create(request):
    # 'GET' 요청 왔을때 리뷰들만 보여주기 
    # 제대로 동작하려나 ?
    def get_review():
        # reviews = get_list_or_404(Review.objects.order_by('-pk')))
        reviews = Review.object.order.by('-pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    # 'POST' 요청으로 왔을 때 리뷰 작성
    def create_review():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_review()

    elif request.method == 'POST':
        return create_review()

# 하나의 영화 리뷰 조회 및 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 'GET' 요청일 땐 리뷰를 보여주기만 함 
    def get_review():
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    # 'PUT' 요청일 때 권한 파악 후 수정 or 거부
    def update_review():
        serializer = ReviewSerializer(review, data=request.data)
        if not request.user.reviews.filter(pk=review.pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 'DELETE' 요청일 때 권한 파악 후 삭제 or 거부
    def delete_review():
        if not request.user.reviews.filter(pk=review.pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)   
        review.delete()
        return Response({'id': review_pk}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return get_review()
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()
    

# 댓글(리뷰)의 목록 조회 및 대댓글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 'GET' 요청 왔을 때, 댓글목록 조회
    def get_comment():
        comments = review.comment_set.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 'POST' 요청 왔을 때, 댓글에 대댓글 생성    
    def create_comment():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_comment()
    elif request.method == 'POST':
        return create_comment()

# 대댓글 조회 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request, comment_pk):
    comment = get_object_or_404(Review, pk=comment_pk)

    # 'GET' 요청 왔을 때, 단일 리뷰의 대댓글 목록 조회
    def get_comment():
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 'PUT' 요청 왔을 때, 대댓글 수정
    def update_comment():
        serializer = CommentSerializer(comment, data=request.data)
        if not request.user.review_comments.filter(pk=comment_pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 

    # 'DELETE' 요청 왔을 때 대댓글 삭제
    def delete_comment():
        if not request.user.review_comments.filter(pk=comment_pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return get_comment()
    elif request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

# 평점 생성 (별점)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 평점 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def rate_update_or_delete(request, rate_pk):
    rate = get_object_or_404(Rate, pk=rate_pk)

    # 'PUT' 요청 왔을 때 평점 수정
    def update_rate():
        serializer = RateSerializer(rate, data=request.data)
        if not request.user.rates.filter(pk=rate_pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 'DELETE' 요청 왔을 때 평점 삭제
    def delete_rate():
        if not request.user.rates.filter(pk=rate_pk).exists():
            return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)
        rate.delete()
        return Response({'id':rate_pk}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        return update_rate()
    elif request.method == 'DELETE':
        return delete_rate()
