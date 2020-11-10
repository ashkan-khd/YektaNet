from django.db import models


class Advertiser(models.Model):
    clicks = models.IntegerField(default=0, null=False)
    views = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)