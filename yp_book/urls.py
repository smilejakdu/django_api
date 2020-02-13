from django.urls import path
from .views import YpBestView

urlpatterns = [
    path('yp_best', YpBestView.as_view())
]
