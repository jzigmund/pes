from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField('Date of creation')

class PackageSet(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # needs to declare set_id (according to DB Model)

class Release(models.Model):
    os_name = models.CharField(max_length=80)
    major_version = models.CharField(max_length=4)
    minor_version = models.CharField(max_length=6)

class Event(models.Model):
    # TODO: revise, not sure if this is the right way how to define and use ENUM
    ACTIONS = (
            ('0', 'New'),
            ('1', 'Removed'),
            ('2', 'Deprecated'),
            ('3', 'Replaced'),
            ('4', 'Splitted'),
            ('5', 'Merged')
    )
    action = models.CharField(max_length=10, choices=ACTIONS)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    in_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE)
    out_packageset = models.ForeignKey(PackageSet, on_delete=models.CASCADE, related_name='+')
