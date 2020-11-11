from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from advertising.models import Advertiser, Ad, Click, View


class AdvertisersView(TemplateView):
    template_name = 'ads.html'

    @staticmethod
    def view_ad(request, ad):
        View.objects.create(ad=ad, ip=request.META.get('REMOTE_ADDR'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisers = Advertiser.objects.all()
        context['advertisers'] = advertisers
        for advertiser in advertisers:
            for ad in advertiser.approved_ads():
                self.view_ad(self.request, ad)
        return context


class AdRedirectView(RedirectView):
    permanent = True

    @staticmethod
    def click_ad(request, ad):
        Click.objects.create(ad=ad, ip=request.META.get('REMOTE_ADDR'))

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        self.click_ad(self.request, ad)
        return ad.link
