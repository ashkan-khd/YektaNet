from django.contrib.auth.models import User


class Advertiser(User):

    def name(self):
        return str(self)

    def clicks(self):
        clicks = 0
        for ad in self.ads.all():
            clicks += ad.clicks.count()
        return clicks

    def approved_ads(self):
        ads = self.ads.filter(is_approved=True)
        return ads

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name) + '- id: ' + str(self.id)
