from django.shortcuts import render, redirect
# 저장 모델 불러오기
from .models import AnimalModel

def animal_view(request):
    # 사용자 인증 여부 확인
    user = request.user.is_authenticated
    if not user:
        return redirect('/sign-in')
    else:
        if request.method == 'GET':
            all_animals = AnimalModel.objects.all().order_by('-happenDt')
            return render(request, 'animal/animal.html', {'animal': all_animals})




