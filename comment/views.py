import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from django.shortcuts import render  # 혹시나 templeates 만질 일이 있지않을까 ... 해서 남겨놓음


# Create your views here.

# 댓글이니 create_at 이 필요하지 않을까?? 생각해볼것

# ctrf == > 일반적인 문자로 가공해서 출력을 해주면 된다.
# values 로 시간을 보내느것보다 객체로 받아서 그 객체를 가공하면 된다.

# 가입한 데이터를 비교를 해야하는것 이기 때문에 ,

# 앱을 나눌때는 models 를 기준으로 나눌려고 하다보면 쉽게 분할을 할 수가 있다. == > 논리적인 근거를 만들어야 한다.
# QuerySet 을 볼것

# 로그인 정보를 남긴다 ===> 서버 테이블이 필요하다 . == >
# except 할꺼면 정확하게 무엇을 할것인지 정확하게 알아야한다.

# from account.models import Account
# Account.objects.get(email='aaa')

# 데이터를 줄땐 JsonReponse 를 하고 굳이 그게아니라 메세지만 주고싶을땐 HttpResponse 를 해주면 된다.

# username = data.get('username' , None)
# email = data.get('email',None)

# requests 쿼리 스트링 에서 처리할때 위와 같이 처리  쿼리 스트링 == ?? url 뒤에 나오는 /?=search 이런거 라고 한다 이거는 url 파라미터 이다.

# 403 은 인증을 받았고 권한 외에서 들어 올려고 하면 ,

# 로그인은 인증 == > 401

#

class CommentView(View):

    def post(self, request):
        comment_data = json.loads(request.body)
        # value_list 를 판별
        try:
            name = comment_data['name']
            comment = comment_data['comment']

            Comment(
                name=comment_data['name'],
                comment=comment_data['comment'],
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message': 'INVALD_KEYS'}, status=400)


def get(self, request):
    comment = Comment.objects.values()  # 한줄로 줄이기
    return JsonResponse({'comment': list(comment)}, status=200)
