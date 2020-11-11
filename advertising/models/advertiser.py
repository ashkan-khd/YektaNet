from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def clicks(self):
        clicks = 0
        for ad in self.ads.all():
            clicks += ad.clicks.count()
        return clicks

    def approved_ads(self):
        ads = self.ads.filter(is_approved=True)
        return ads

    def __str__(self):
        return str(self.name)
