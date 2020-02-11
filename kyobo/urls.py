from django.urls import path
from .views import KyoboBestView

urlpatterns = [
    path('/kyobo_best', KyoboBestView.as_view())
]
