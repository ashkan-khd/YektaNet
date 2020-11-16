from django import forms
from django.contrib import admin
from django.contrib.auth.hashers import make_password

from user.models import Advertiser


class UserBaseForm(forms.ModelForm):
    def clean_password(self):
        if 'password' in self.changed_data:
            return make_password(self.data['password'])
        else:
            return self.data['password']


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'clicks']
    readonly_fields = ('clicks',)
    form = UserBaseForm

    class Meta:
        model = Advertiser
