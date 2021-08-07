from django.db import models

# django에서 기본으로 제공하는 auth로 로그인 기능 설정
from django.contrib.auth.models import AbstractUser


# 설정 파일을 장고가 알아서 관리(4장 6번째)
from django.conf import settings


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    # django 에서 기본적으로 제공하는 기능 사용하고, 추가로 설정한다는 뜻
    # 가입 목적
    purpose = models.CharField(max_length=256, default='')
    # 성별
    sex = models.CharField(max_length=20, default='')
    # 연령
    age = models.CharField(max_length=20, default='')

    # 시
    city = models.CharField(max_length=20, default='')

    # 구
    district = models.CharField(max_length=20, default='')

    # found 게시물 수
    found_cnt = models.IntegerField(default=0)

    # 전화번호 (실종자의 경우에만 필수기입)
    phone_num = models.CharField(max_length=20, default='')



