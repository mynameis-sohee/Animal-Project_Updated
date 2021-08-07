from django.contrib import admin
from django.urls import path
from . import views
# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('missing/', views.found, name='found'),
    path('missing/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    path('missing/<int:id>', views.detail_tweet, name='detail_tweet')
]


# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)