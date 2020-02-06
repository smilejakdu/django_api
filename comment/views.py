import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from django.shortcuts import render  # 혹시나 templeates 만질 일이 있지않을까 ... 해서 남겨놓음


# Create your views here.


class CommentView(View):

    def post(self, request):
        comment_data = json.loads(request.body)
        email = comment_data['email']
        comment = comment_data['comment']
        print('email', email)
        print('comment', comment)

        if comment is None or comment == '':
            return JsonResponse({'comment': '내용을 입력하세요'})

        if email is not None and comment is not None or comment == '':
            Comment(
                email=comment_data['email'],
                comment=comment_data['comment'],
            ).save()
            return HttpResponse(status=200)

    def get(self, request):
        comment = Comment.objects.values()

        return JsonResponse({'comment': list(comment)}, status=200)
