from django.views.generic import RedirectView
from rest_framework.generics import get_object_or_404

from advertising.models import Ad, Click


class AdRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.click_ad(ad, kwargs['ip'])
        return ad.link
