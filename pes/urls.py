from django.urls import path

from . import views

app_name = 'pes'
urlpatterns = [
        path('', views.EventListView.as_view(), name="index"),
        path('new', views.ReleaseCreate.as_view(), name="new"),
]
