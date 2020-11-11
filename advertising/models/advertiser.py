from django.db import models


class Advertiser(models.Model):
    clicks = models.PositiveIntegerField(default=0, null=False)
    views = models.PositiveIntegerField(default=0, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.name)
