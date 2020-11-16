from django.db.models import Count, FloatField, Case, When, Sum, IntegerField
from django.db.models.functions import Cast


def annotate_clicks_views(annotator):
    def inner(query, fields, hour):
        query = query.annotate(views_count=Case(
            When(views__time__hour__range=[hour, hour + 1], then=Count('views', distinct=True)),
            output_field=IntegerField()), clicks_count=Case(
            When(clicks__time__hour__range=[hour, hour + 1], then=Count('clicks', distinct=True)),
            output_field=IntegerField()))

        fields += ['clicks_count', 'views_count']
        query, fields = annotator(query, fields, hour)
        return query, fields

    return inner


def annotate_ctr(annotator):
    def inner(query, fields, hour):
        query = query.annotate(ctr=Case(
            When(views_count__gt=0, then=Cast('clicks_count', FloatField()) / Cast('views_count', FloatField())),
            output_field=FloatField()))
        fields += ['ctr']
        query, fields = annotator(query, fields, hour)
        return query, fields

    return inner


@annotate_clicks_views
@annotate_ctr
def annotate_hour_filtered(query, fields, hour):
    return query, fields
