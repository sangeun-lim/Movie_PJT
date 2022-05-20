from rest_framework import serializers
from ..models import Rate

class RateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rate
        field = '__all__'
        read_only_fields = ('movie', 'user')