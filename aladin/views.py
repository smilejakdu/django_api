import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Aladin


# Create your views here.

class AladinBestView(View):
    def get(self, request):
        aladin_book = Aladin.objects.values()

        return JsonResponse({'title': list(aladin_book)}, status=200)
