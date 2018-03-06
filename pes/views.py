from django.views.generic.list import ListView
from .models import Event


class EvenListView(ListView):
    model = Event
