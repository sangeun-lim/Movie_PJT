from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like/', views.like_movie),
    # comments
    path('<int:movie_id>/comments/', views.create_comment),
    path('<int:movie_id>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]