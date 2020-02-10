import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


# except Account.DoesNotExist: 란 ? == > 만약에 사용할게 없다면
# except KeyError : ??  == > 키 에러에 대한 내용

# 항상 python manage.py shell 로 확인을 해줄것 . objects . == > 무엇이 있는지 확인을 해볼것

# 앱 이름으로 할것
# 서버 개발자 끼리 보는거라 생각해서 status 코드를 생각할것

# 틀렸는데 200 이면 안된다 == > 상황에 따라서 status 를 봐야한다.  == > 보안을 위해서

# cmd + g 누르면 번호로 이동
# cmd + option + 방향키로 할것

# values_list 는 무엇인가 ??
# flat 는 무엇인가 ?

# 찾을때는 ?? django document == > querysetapi reference 검색을 해볼것
# =============================

# 함수와 class 붙여야 한다.
#  try 빈것이 인지 확인  try 는 키에러 F string 으로 바꿀것
# Http response 로 해서 404 로 할것

# else 를 생략 할수 있다


class AccountView(View):  # 회원가입

    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email=data['email']).exists():
            return JsonResponse({'email': '존재하는 이메일 입니다.'}, status=200)

        if data['password'] is None or data['password'] == '':
            return JsonResponse({'password': 'password 를 입력하세요.'}, status=200)

        Account(
            email=data['email'],
            name=data['name'],
            password=data['password'],
        ).save()

        return JsonResponse({'Success': '안녕하세요'}, status=200)

    def get(self, request):  # 확인하기 위해서
        return JsonResponse({"회원가입페이지": ''}, status=200)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])
                if user.password == data['password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

