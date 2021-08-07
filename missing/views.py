from django.shortcuts import render, redirect

# 글쓰기 모델 불러오기 - post 위함
from .models import TweetMissingModel

# 로그아웃 기능 - 인증된 auth 정보 없애기위해, 로그인 정보 갖고오기
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def found(request):
    #  사용자 인증 여부 확인
    user = request.user.is_authenticated
    if not user:
        return redirect('/sign-in')
    else:

        if request.method == 'GET':
            all_tweet = TweetMissingModel.objects.all().order_by('-created_at')
            return render(request, 'missing/missing.html', {'tweet': all_tweet})


        elif request.method == 'POST':
            # 현재 로그인 한 사용자를 불러오기
            user = request.user
            # 글쓰기 모델 가져오기
            my_tweet = TweetMissingModel()
            # 모델에 사용자 저장
            my_tweet.author = user
            # 모델에 글 저장
            my_tweet.content = request.POST.get('my-content', '')
            my_tweet.city = request.POST.get('my-location1', '')
            my_tweet.district = request.POST.get('my-location2', '')
            my_tweet.neighborhood = request.POST.get('my-location3', '')
            my_tweet.category = request.POST.get('my-category', '')
            my_tweet.color = request.POST.get('my-color', '')
            my_tweet.size = request.POST.get('my-size', '')
            my_tweet.phone_num = request.POST.get('my-phone_num', '')
            my_tweet.image = request.POST.get('my-image', '')

            my_tweet.save()

            return redirect('/missing')


@login_required
def delete_tweet(request, id):
    if request.method == 'GET':
        my_tweet = TweetMissingModel.objects.get(id=id)
        my_tweet.delete()
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/missing')

@login_required
def detail_tweet(request, id):
    tweet = TweetMissingModel.objects.get(id=id)
    return render(request,'missing/missing_detail.html', {'tweet':tweet})

