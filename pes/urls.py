from django.urls import path

from .views import EventListView, ReleaseCreateView, event_create_view, ReleaseListView

app_name = 'pes'
urlpatterns = [
        path('events', EventListView.as_view(), name="index"),
        path('release', ReleaseListView.as_view(), name="release"),
        path('release/new', ReleaseCreateView.as_view(), name="new_release"),
        path('events/new', event_create_view, name="new_event"),
]
