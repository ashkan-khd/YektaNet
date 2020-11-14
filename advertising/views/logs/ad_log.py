from django.db.models import Count, FloatField, Avg
from django.db.models.functions import Cast
from rest_framework import views
from rest_framework.response import Response

from advertising.models import Ad
from advertising.views.logs import annotate_general


class AdLogView(views.APIView):

    def get(self, request):
        query, fields = annotate_general(Ad.objects.all(),
                                         ['click_view_delay', 'views_count_total', 'clicks_count_total',
                                          'ctr_total'])
        if request.query_params.get('hour', None):
            hour = int(request.query_params.get('hour'))
            query = query.filter(clicks__time__hour__range=[hour, hour + 1]) \
                .annotate(clicks_count=Count('clicks', distinct=True)
                          , views_count=Count('views', distinct=True)) \
                .annotate(ctr=Cast('clicks_count', FloatField()) / Cast('views_count', FloatField()))
            fields += ['clicks_count', 'views_count', 'ctr']
        if request.query_params.get('id', None):
            query = query.filter(id=request.query_params['id'])
        return Response(data=query.values(*fields))
