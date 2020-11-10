from django.contrib import admin

# Register your models here.
from advertising.models import Ad, Advertiser

admin.site.register(Advertiser)
admin.site.register(Ad)