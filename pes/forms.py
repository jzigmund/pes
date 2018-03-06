from django.forms import ModelForm
from .models import Package, PackageSet, Release, Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['created', 'modified']


class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = '__all__'


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['name']


class PackageSetForm(ModelForm):
    class Meta:
        model = PackageSet
        fields = '__all__'
