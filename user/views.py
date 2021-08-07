# render: html화면을 보여준다.
from django.shortcuts import render, redirect

# 나의 위치와 동일한 애중에 models를 갖고 온다.
from .models import UserModel



from django.http import HttpResponse

# 로그아웃 기능 - 인증된 auth 정보 없애기
from django.contrib.auth.decorators import login_required

# 사용자가 DB 안에 있는지 검사 - exist_user
from django.contrib.auth import get_user_model

# post에서 작성한 password와 암호화된 password 비교 시 사용
from django.contrib import auth





def signup_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        purpose = request.POST.get('purpose', '')
        age = request.POST.get('age', '')
        sex = request.POST.get('sex', '')
        city = request.POST.get('city', '')
        district = request.POST.get('district', '')

        # 010-0000-0000 형태로 저장
        phone_num = request.POST.get('phone_num', '').format(''.join(char for char in request.POST.get('phone_num', '') if char.isalnum()))


        if password != password2:
            return render(request, 'user/signup.html', {'error':"비밀번호가 같지 않아요!"})
        else:
            if username == '' or password == '' or purpose == '' or age == '' or sex == '' or phone_num == '':
                return render(request, 'user/signup.html', {'error':"빈 칸이 없는지 다시 확인해주세요!"})
            if len(password) < 5:
                return render(request, 'user/signup.html', {'error':"비밀번호는 최소 5글자 이상이어야 해요!"})
            
            if len(username) < 5 :
                return render(request, 'user/signup.html', {'error':"ID는 최소 5글자 이상이어야 해요!"})

            if str(phone_num)[:3] != '010':
                return render(request, 'user/signup.html', {'error':"휴대폰 번호를 다시 한 번 확인해주세요!"})

            if len(phone_num) <= 9 :
                return render(request, 'user/signup.html', {'error':"휴대폰 번호를 다시 한 번 확인해주세요!"})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error':"같은 ID를 가진 사용자가 존재해요! 새로운 ID를 입력해주세요!"})
            else:
                UserModel.objects.create_user(username=username, password=password, purpose=purpose, age=age, sex=sex, city=city, district=district, phone_num=phone_num)
                return redirect('/sign-in')



def signin_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error':'이름 혹은 패스워드가 일치하지 않습니다.'})



# 로그아웃 - 인증된 정보를 없애기
# @login_required - 로그인 한 사용자만 접근할 수 있는 데코레이터
@login_required
def logout_view(request):
    # 인증 되어있는 정보를 없애기
    auth.logout(request)
    return redirect("/")