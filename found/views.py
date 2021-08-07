from django.shortcuts import render, redirect

# 글쓰기 모델 불러오기 - post 위함
from .models import TweetFoundModel

# 로그아웃 기능 - 인증된 auth 정보 없애기위해, 로그인 정보 갖고오기
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# 네이버 SMS API 위해 import
import hmac, hashlib, base64
import time, requests, json


def found(request):
    #  사용자 인증 여부 확인
    user = request.user.is_authenticated
    if not user:
        return redirect('/sign-in')
    else:

        if request.method == 'GET':
            all_tweet = TweetFoundModel.objects.all().order_by('-created_at')
            return render(request, 'found/found.html', {'tweet': all_tweet})


        elif request.method == 'POST':
            # 현재 로그인 한 사용자를 불러오기
            user = request.user
            # 글쓰기 모델 가져오기
            my_tweet = TweetFoundModel()
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
            if request.POST.get('my-phone_num') == 'yes':
                my_tweet.phone_num = user.phone_num
            else:
                my_tweet.phone_num = request.POST.get('my-phone', '')
            my_tweet.image = request.FILES['my-image']

            my_tweet.save()

            return redirect('/found')


@login_required
def delete_tweet(request, id):
    if request.method == 'GET':
        my_tweet = TweetFoundModel.objects.get(id=id)
        my_tweet.delete()
        messages.info(request, 'Three credits remain in your account.')
        return redirect('/found')


@login_required
def detail_tweet(request, id):
    tweet = TweetFoundModel.objects.get(id=id)
    user = request.user
    if request.method == 'GET':
        return render(request,'found/found_detail.html', {'tweet':tweet})

    elif request.method == 'POST':
        sid = "ncp:sms:kr:보안:phone_number"
        sms_uri = "/sms/v2/services/ncp:sms:kr:보안:phone_number/messages"
        sms_url = "https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:보안:phone_number/messages"
        sec_key = "{보안}"

        acc_key_id = "보안"
        acc_sec_key = b'보안'

        stime = int(float(time.time()) * 1000)

        hash_str = "POST {}\n{}\n{}".format(sms_uri, stime, acc_key_id)

        digest = hmac.new(acc_sec_key, msg=hash_str.encode('utf-8'), digestmod=hashlib.sha256).digest()
        d_hash = base64.b64encode(digest).decode()

        from_no = "보안"

        # 로그인 유저(주인 추정) 번호 - 특수기호 제거
        user_no = "{}".format(''.join(char for char in user.phone_num if char.isalnum()))

        # 목격자 전화번호 - 특수기호 제거
        to_no = "{}".format(''.join(char for char in tweet.phone_num if char.isalnum()))
        message = "[우리동네멍냥] 목격하신 동물 주인 {}님께서 귀하의 전화를 기다리고 있습니다.".format(user_no)

        msg_data = {
            'type': 'SMS',
            'countryCode': '82',
            'from': "{}".format(from_no),
            'contentType': 'COMM',
            'content': "{}".format(message),
            'messages': [{'to': "{}".format(to_no)}]
        }

        response = requests.post(
            sms_url, data=json.dumps(msg_data),
            headers={"Content-Type": "application/json; charset=utf-8",
                     "x-ncp-apigw-timestamp": str(stime),
                     "x-ncp-iam-access-key": acc_key_id,
                     "x-ncp-apigw-signature-v2": d_hash
                     }
        )
        print(response.text)
        tweet = TweetFoundModel.objects.get(id=id)

        return render(request,'found/found_detail.html', {'tweet':tweet})



