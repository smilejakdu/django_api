import json

from kyobo.models import Kyobo
from .models import BestSearch
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import BestSearch


# Create your views here.

class BestSearchView(View):

    def post(self, request):
        BestSearch.objects.all().delete()
        data = json.loads(request.body)

        if data['title'] is None or data['title'] == '':
            return JsonResponse({'title': '없는데??'}, status=405)

        BestSearch(
            title=data['title']
        ).save()

        return JsonResponse({'title': '받았습니다.'}, status=200)

    def get(self, request):
        title = BestSearch.objects.values()
        kyobo_book = Kyobo.objects.values()
        title = list(title)
        search_title = ''
        for t in title:
            search_title = t['title']
        search_title = str(search_title)
        for x in kyobo_book:
            x = str(x)
            print(x)
            if search_title in x:
                print(x)
                return JsonResponse({'title': '{}'.format(x)}, status=200)
