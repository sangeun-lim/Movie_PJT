from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_create),
    path('<int:review_pk>/', views.review_update_or_delete),
    path('<int:review_pk>/like/', views.review_like),
    path('<int:review_pk>/comments/', views.comment_create),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]