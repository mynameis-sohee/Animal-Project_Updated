from django.contrib import admin
from django.urls import path
from . import views



# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('found/', views.found, name='found'),
    path('found/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    path('found/<int:id>', views.detail_tweet, name='detail_tweet'),
]
