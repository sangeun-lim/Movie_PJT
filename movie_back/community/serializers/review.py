from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review
from .comment import CommentSerializer

User = get_user_model()

class ReviewListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count','created_at','updated_at')


class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    review_comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'review_comments', 'like_users', 'created_at', 'updated_at')
        # depth = 1
        # read_only_fields =('user', 'like_users',)