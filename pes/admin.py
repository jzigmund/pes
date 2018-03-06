from django.contrib import admin
from .models import Package, PackageSet, Event, Release
# Register your models here.
admin.site.register(PackageSet)
admin.site.register(Package)
admin.site.register(Event)
admin.site.register(Release)
