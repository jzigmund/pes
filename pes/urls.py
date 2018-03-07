from django.urls import path

from .views import EventListView, ReleaseCreateView

app_name = 'pes'
urlpatterns = [
        path('', EventListView.as_view(), name="index"),
        path('new', ReleaseCreateView.as_view(), name="new"),
]
