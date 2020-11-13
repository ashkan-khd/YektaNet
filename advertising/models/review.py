from django.db import models
from django.db.models import CASCADE

from advertising.models import Ad


class Review(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    class Meta:
        abstract: True


class Click(Review):
    view_delay = models.DurationField()
    ad = models.ForeignKey(
        to=Ad,
        related_name='clicks',
        on_delete=CASCADE
    )

    def __str__(self):
        return str(self.ip) + '- ' + str(self.ad)


class View(Review):
    ad = models.ForeignKey(
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )

    def __str__(self):
        return str(self.ip) + '- ' + str(self.ad)
