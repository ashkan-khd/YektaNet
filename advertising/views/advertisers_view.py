from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView, RedirectView

from advertising.models import Advertiser, Ad, Click, View


class AdvertisersView(TemplateView):
    template_name = 'ads.html'

    @staticmethod
    def view_ad(ad, ip):
        View.objects.create(ad=ad, ip=ip)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisers = Advertiser.objects.all()
        context['advertisers'] = advertisers
        for advertiser in advertisers:
            for ad in advertiser.approved_ads():
                self.view_ad(ad, kwargs['ip'])
        return context


class AdRedirectView(RedirectView):
    permanent = False

    @staticmethod
    def click_ad(ad, ip):
        query = Click.objects.create(ad=ad,
                                     ip=ip,
                                     view_delay=timezone.now() - ad.views.filter(ip=ip).order_by('-time').first().time)

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        self.click_ad(ad, kwargs['ip'])
        return ad.link
