from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# 리뷰(댓글)
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    title = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 리뷰에 대한 댓글 (대댓글)
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rates')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rates')
    score = models.IntegerField(validators= [MaxValueValidator(5),MinValueValidator(1)])