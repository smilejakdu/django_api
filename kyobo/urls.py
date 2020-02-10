from django.urls import path
from .views import KyoboBestView

urlpatterns = [
    path('/best', KyoboBestView.as_view())
]
