from django.utils import timezone
from django.views.generic import RedirectView
from rest_framework.generics import get_object_or_404

from advertising.models import Ad, Click


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
