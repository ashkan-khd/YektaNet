from django.utils import timezone
from django.db import models
from django.db.models import CASCADE

from advertising.models import Ad
from utility.models import BaseHistoryModel


class BaseAdEvent(BaseHistoryModel):
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True


class Click(BaseAdEvent):
    view_delay = models.DurationField()
    ad = models.ForeignKey(
        to=Ad,
        related_name='clicks',
        on_delete=CASCADE
    )

    @staticmethod
    def click_ad(ad, ip):
        Click.objects.create(ad=ad,
                             ip=ip,
                             view_delay=timezone.now() - ad.views.filter(ip=ip).order_by('-time').first().time)

    def __str__(self):
        return str(self.ip) + '- ' + str(self.ad)


class View(BaseAdEvent):
    ad = models.ForeignKey(
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )

    @staticmethod
    def view_ad(ad, ip):
        View.objects.create(ad=ad, ip=ip)

    def __str__(self):
        return str(self.ip) + '- ' + str(self.ad)
