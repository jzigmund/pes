from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PackageSet(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # TODO: set to id?
    set_id = models.IntegerField(null=True, blank=True)


class Release(models.Model):
    os_name = models.CharField(max_length=80)
    major_version = models.CharField(max_length=4)
    minor_version = models.CharField(max_length=6)


class Event(models.Model):
    ACTIONS = (
            ('0', 'New'),
            ('1', 'Removed'),
            ('2', 'Deprecated'),
            ('3', 'Replaced'),
            ('4', 'Split'),
            ('5', 'Merged')
    )
    action = models.IntegerField(choices=ACTIONS)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    in_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE, related_name='in')
    out_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE, related_name='out')
    description = models.TextField(blank=True, null=True)
    docstring = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
