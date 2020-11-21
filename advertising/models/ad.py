

from django.db import models
from django.db.models import PROTECT

from user.models import Advertiser
from utility.models import BaseHistoryModel


class Ad(BaseHistoryModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    image_url = models.CharField(max_length=255, null=False, blank=False)
    link = models.CharField(max_length=255, null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    advertiser = models.ForeignKey(
        to=Advertiser,
        related_name='ads',
        on_delete=PROTECT
    )

    def __str__(self):
        return str(self.title) + '-' + ' from ' + str(self.advertiser) + '- id: ' + str(self.id)
