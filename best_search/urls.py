from django.urls import path
from .views import BestSearchView

urlpatterns = [
    path('/search_best', BestSearchView.as_view())
]
