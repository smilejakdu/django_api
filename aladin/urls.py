from django.urls import path
from .views import AladinBestView

urlpatterns = [
    path('/aladin_best', AladinBestView.as_view())
]
