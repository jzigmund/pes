from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from .models import Event, Release


class EventListView(generic.ListView):
    model = Event

class ReleaseCreate(generic.CreateView):
    model = Release
    fields =['os_name', 'major_version', 'minor_version']
    success_url = reverse_lazy('pes:event_list')
