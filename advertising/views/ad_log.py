from django.db.models import Count, FloatField, Avg
from django.db.models.functions import Cast
from rest_framework import views
from rest_framework.response import Response

from advertising.models import Ad


def annotate_click_view_delay(annotator):
    def inner(query, fields):
        query = query.annotate(click_view_delay=Avg('clicks__view_delay'))
        fields += ['click_view_delay']
        annotator(query, fields)

    return inner


@annotate_click_view_delay
def annotate_general(query, fields):
    query = query.annotate(views_count_total=Count('views', distinct=True),
                           clicks_count_total=Count('clicks', distinct=True)) \
        .exclude(views_count_total=0) \
        .annotate(ctr_total=Cast('clicks_count_total', FloatField()) / Cast('views_count_total', FloatField()))
    fields += ['id', 'ctr_total', 'clicks_count_total', 'views_count_total']


class AdLogView(views.APIView):

    def get(self, request):
        query = Ad.objects.all()
        fields = []
        annotate_general(query, fields)
        # query = query.annotate(click_view_delay=Avg('clicks__view_delay')) \
        #     .annotate(views_count_total=Count('views', distinct=True),
        #               clicks_count_total=Count('clicks', distinct=True)) \
        #     .exclude(views_count_total=0) \
        #     .annotate(ctr_total=Cast('clicks_count_total', FloatField()) / Cast('views_count_total', FloatField()))
        # fields = ['id', 'ctr_total', 'click_view_delay', 'clicks_count_total', 'views_count_total']
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
