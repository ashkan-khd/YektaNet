from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from advertising.models import Advertiser, Ad
from advertising.services import click_ad


class AdvertisersView(TemplateView):
    template_name = 'ads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()
        return context


class AdRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        click_ad(ad)
        return ad.link
