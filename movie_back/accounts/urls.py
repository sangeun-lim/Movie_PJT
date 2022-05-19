from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('mypage/<username>/', views.mypage),
]
