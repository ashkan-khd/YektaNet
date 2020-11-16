from django.contrib import admin

from advertising.models import Ad, Click, View


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    def Clicks(self, obj):
        return obj.clicks.count()

    def Views(self, obj):
        return obj.views.count()

    list_display = ['__str__', 'Clicks', 'Views', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['title']
    readonly_fields = ('create_time',)

    class Meta:
        model = Ad


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    readonly_fields = ('time', 'view_delay')

    class Meta:
        model = Click


@admin.register(View)
class ClickAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

    class Meta:
        model = View
