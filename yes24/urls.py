from django.urls import path
from .views import YesBestView

urlpatterns = [
    path('yes_best', YesBestView.as_view())
]
