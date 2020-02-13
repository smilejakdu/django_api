import json
from django.views import View
from .models import Kyobo
from django.http import HttpResponse, JsonResponse


# Create your views here.

class KyoboBestView(View):
    def get(self, request):
        kyobo_book = Kyobo.objects.values()

        return JsonResponse({'title': list(kyobo_book)}, status=200)
