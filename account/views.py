import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


class AccountView(View):

    def post(self, request):  # post 는 파일 전송
        data = json.loads(request.body)
        # post data :  {'email': 'sory1@gmail.com', 'password': '1'}
        Account(
            email=data['email'],
            password=data['password'],
        ).save()

        return HttpResponse(status=200)

    def get(self, request):  # URI 형식으로 웹 서버측 리소스(데이터)를 요청
        try:
            user_get = json.loads(request.body)
            account_data = Account.objects.values()
            print('account_data : ', list(account_data))
            email = user_get['email']
            password = user_get['password']
            if email not in account_data:
                return JsonResponse({'email': email, 'password': password}, status=200)
            else:
                return JsonResponse({'account': 'not found'}, status=200)
        except:
            return JsonResponse({'not found': "이메일과 비밀번호 입력"})
