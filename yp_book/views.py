import json
from django.views import View
from .models import YpBook

from django.http import HttpResponse, JsonResponse


# Create your views here.

class YpBestView(View):
    def get(self, request):
        yp_book = YpBook.objects.values()

        return JsonResponse({'title': list(yp_book)}, status=200)

