from django.db import models

# 다른 모델을 불러온다.
from user.models import UserModel
# Create your models here.

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class TweetFoundModel(models.Model):
    class Meta:
        db_table = "tweet_found"
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=20, default='')
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    image = models.ImageField(upload_to="found/%Y-%m-%d")
