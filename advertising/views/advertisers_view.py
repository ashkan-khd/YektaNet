from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from advertising.models import Advertiser, View


class AdvertisersView(ListAPIView):
    queryset = Advertiser.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ads.html'

    @staticmethod
    def view_ad(ad, ip):
        View.objects.create(ad=ad, ip=ip)

    def get(self, request, *args, **kwargs):
        for advertiser in self.queryset.all():
            for ad in advertiser.approved_ads():
                self.view_ad(ad, kwargs['ip'])
        return Response({'advertisers': self.queryset.all()}, template_name=self.template_name)