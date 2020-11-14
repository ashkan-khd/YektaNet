from django.db.models import Count, FloatField
from django.db.models.functions import Cast


def filter_by_hour(annotator):
    def inner(query, fields, hour):
        query = query.filter(clicks__time__hour__range=[hour, hour + 1])
        query, fields = annotator(query, fields, hour)
        return query, fields

    return inner


def annotate_clicks_views(annotator):
    def inner(query, fields, hour):
        query = query.annotate(views_count=Count('views', distinct=True),
                               clicks_count=Count('clicks', distinct=True))
        fields += ['clicks_count', 'views_count']
        query, fields = annotator(query, fields, hour)
        return query, fields

    return inner


def annotate_ctr(annotator):
    def inner(query, fields, hour):
        query = query.exclude(views_count=0) \
            .annotate(ctr=Cast('clicks_count', FloatField()) / Cast('views_count', FloatField()))
        fields += ['ctr']
        query, fields = annotator(query, fields, hour)
        return query, fields

    return inner


@filter_by_hour
@annotate_clicks_views
@annotate_ctr
def annotate_hour_filtered(query, fields, hour):
    return query, fields