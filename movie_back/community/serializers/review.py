from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields ='__all__'
        depth = 1
        read_only_fields =('user', 'like_users',)