import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


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


class LoginView(View):  # 로그인
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email=data['email']).exists():
            # 만약에 email 이 존재한다면 else == > error
            if data['password'] == Account.objects.get(email=data['email']).password:
                return JsonResponse({'email': "{} 님 안녕하세요.".format(data['email'])}, status=200)
            else:
                return JsonResponse({"error": "error"}, status=401)
        else:
            return JsonResponse({"error": "error"}, status=401)

    def get(self, request):  # 확인하기 위해서
        return JsonResponse({'로그인페이지': ''}, status=200)
