from django.db.models import Count, FloatField, Avg
from django.db.models.functions import Cast


def annotate_click_view_delay(annotator):
    def inner(query, fields):
        query = query.annotate(click_view_delay=Avg('clicks__view_delay'))
        fields += ['click_view_delay']
        query, fields = annotator(query, fields)
        return query, fields

    return inner


def annotate_total_clicks_views(annotator):
    def inner(query, fields):
        query = query.annotate(views_count_total=Count('views', distinct=True),
                               clicks_count_total=Count('clicks', distinct=True))
        fields += ['clicks_count_total', 'views_count_total']
        query, fields = annotator(query, fields)
        return query, fields

    return inner


def annotate_total_ctr(annotator):
    def inner(query, fields):
        query = query.exclude(views_count_total=0) \
            .annotate(ctr_total=Cast('clicks_count_total', FloatField()) / Cast('views_count_total', FloatField()))
        fields += ['ctr_total']
        query, fields = annotator(query, fields)
        return query, fields

    return inner


@annotate_click_view_delay
@annotate_total_clicks_views
@annotate_total_ctr
def annotate_general(query, fields):
    return query, fields


