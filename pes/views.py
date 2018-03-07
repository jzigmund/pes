from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .forms import *

from .models import Event, Release

class EventListView(generic.ListView):
    model = Event


def event_create_view(request):
    event_form = EventForm()
    package_set_form = PackageSetForm()
    package_form = PackageForm()

    if request.POST:
        event_form = EventForm(request.POST)
        package_set_form = PackageSetForm(request.POST)
        package_form = PackageForm(request.POST)

        if event_form.is_valid() and package_form.is_valid() and package_set_form.is_valid():
            event_form.save(commit=False)
            package_set_form.save(commit=False)

            package_set_form.package = package_form.save()
            ps = package_set_form.save()
            event_form.in_packageset = ps
            event_form.out_packageset = ps
            event_form.save()

            return HttpResponseRedirect('')

    template = 'pes/event_create.html'
    context = {'event_form': event_form, 'package_set_form': package_set_form, 'package_form': package_form}
    return render(request, template_name=template, context=context)

class ReleaseCreateView(generic.CreateView):
    model = Release
    fields =['os_name', 'major_version', 'minor_version']
