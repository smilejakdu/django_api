import json
from django.views import View
from .models import Yes
from django.http import HttpResponse, JsonResponse


# Create your views here.

class YesBestView(View):
    def get(self, request):
        yes_book = Yes.objects.values()

        return JsonResponse({'title': list(yes_book)}, status=200)
