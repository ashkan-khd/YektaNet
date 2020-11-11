from django.contrib import admin

from advertising.models import Ad, Advertiser, Click


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    readonly_fields = ('clicks',)

    class Meta:
        model = Advertiser


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    def Clicks(self, obj):
        return obj.clicks.count()

    def Views(self, obj):
        return obj.views.count()

    list_display = ['__str__', 'Clicks', 'Views']

    class Meta:
        model = Ad


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

    class Meta:
        model = Click
