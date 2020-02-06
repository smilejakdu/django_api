import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


class AccountView(View):

    def post(self, request):  # post 는 파일 전송
        data = json.loads(request.body)
        account_data = Account.objects.values()
        # post data :  {'email': 'sory1@gmail.com', 'password': '1'}
        email = data['email']
        password = data['password']
        name = data['name']
        print('email', email)
        print('password', password)

        if email in list(account_data):
            return JsonResponse({'email': '존재하는 이메일 입니다.'})

        if password is None or password == '':
            return JsonResponse({'password': 'password 를 입력하세요.'})

        Account(
            email=email,
            name=name,
            password=password,
        ).save()  # 이메일과 비밀번호 저장

        return JsonResponse({'email': '안녕하세요'}, status=200)

    def get(self, request):
        return JsonResponse({'login': 'login 하세요.'})
