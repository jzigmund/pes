from django.urls import path

from .views import EvenListView

urlpatterns = [
        path('', EvenListView.as_view(), name="index")
]
