from django.utils import timezone
from django.views.generic import RedirectView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from advertising.models import Ad, Click
from advertising.views.ad_view.logs.annotators import annotate_general, annotate_hour_filtered
from advertising.views.ad_view.serializers import AdSerializer


class ListCreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    pass


class AdViewSet(ListCreateRetrieveViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    @staticmethod
    def annotate_logs(request, query):
        query, fields = annotate_general(query, ['id'])

        if request.query_params.get('hour', None):
            hour = int(request.query_params.get('hour'))
            query, fields = annotate_hour_filtered(query, fields, hour)

        return query.values(*fields)

    @action(detail=True, url_path='log', url_name='log')
    def log(self, request, pk=None):
        return Response(data=self.annotate_logs(request, self.queryset.filter(pk=pk)))

    @action(detail=False, url_path='log', url_name='log')
    def logs(self, request):
        return Response(data=self.annotate_logs(request, self.queryset))


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