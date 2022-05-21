from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Review
from .models import Comment
from .serializers.comment import CommentSerializer
from .serializers.review import ReviewSerializer
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
            comments = review.review_comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_comment()
    elif request.method == 'POST':
        return create_comment()


# 댓글 조회 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 'GET' 요청 왔을 때, 단일 리뷰의 댓글 목록 조회
    def get_comment():
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 'PUT' 요청 왔을 때, 댓글 수정
    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.review_comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data) 
        # if not request.user.review_comments.filter(pk=comment_pk).exists():
        #     return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN) 

    # 'DELETE' 요청 왔을 때 댓글 삭제
    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.review_comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data) 

        # if not request.user.review_comments.filter(pk=comment_pk).exists():
        #     return Response({'detail': '수정 권한 없음!'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        return get_comment()
    elif request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else :
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)