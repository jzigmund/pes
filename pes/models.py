from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PackageSet(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # TODO: set to id?
    set_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Release(models.Model):
    os_name = models.CharField(max_length=80)
    major_version = models.CharField(max_length=4)
    minor_version = models.CharField(max_length=6)

    def __str__(self):
        return "{OS} {MAJOR}.{MINOR}".format(OS=self.os_name, MAJOR=self.major_version, MINOR=self.minor_version)


class Event(models.Model):
    ACTIONS = (
            (0, 'New'),
            (1, 'Removed'),
            (2, 'Deprecated'),
            (3, 'Replaced'),
            (4, 'Split'),
            (5, 'Merged')
    )
    action = models.IntegerField(choices=ACTIONS)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    in_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE)
    out_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE, related_name='+')
    description = models.TextField(blank=True, null=True)
    docstring = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{PKG} {ACTION}".format(PKG=self.in_packageset.package.name, ACTION=self.ACTIONS[self.action][1])
