
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from rest_framework.response import Response

from advertising.models import Ad
from advertising.views.ad_views.logs.annotators import annotate_general, annotate_hour_filtered
from advertising.views.ad_views.serializers import AdSerializer


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


