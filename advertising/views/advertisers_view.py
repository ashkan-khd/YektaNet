from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from advertising.models import Advertiser, Ad, Click


class AdvertisersView(TemplateView):
    template_name = 'ads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()
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
