from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MypageSerializer


User = get_user_model()


# 로그인한 자신만 자신의 마이페이지에 갈수있게하기

# isAuthenticated 를 추가해야되려나요??

@api_view(['GET'])
def mypage(request, username):
    user = get_object_or_404(User ,username=username)
    serializer = MypageSerializer(user)
    return Response(serializer.data)