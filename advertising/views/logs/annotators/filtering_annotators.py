def annotate_clicks_views(annotator):
    def inner(query, fields, data, hour):

        for ad in query.all():
            ad_dict = query.filter(pk=ad.id).values(*fields)[0]
            ad_dict['clicks_count'] = ad.clicks.filter(time__hour__range=[hour, hour + 1]).count()
            ad_dict['views_count'] = ad.views.filter(time__hour__range=[hour, hour + 1]).count()
            data.append(ad_dict)

        data = annotator(query, fields, data, hour)
        return data

    return inner


def annotate_ctr(annotator):
    def inner(query, fields, data, hour):
        for ad_dict in data:
            if ad_dict.get('views_count', 0) != 0:
                ad_dict['ctr'] = ad_dict['clicks_count']/ad_dict['views_count']
            else:
                ad_dict['ctr'] = None

        data = annotator(query, fields, data, hour)
        return data

    return inner


@annotate_clicks_views
@annotate_ctr
def annotate_hour_filtered(query, fields, data, hour):
    return data
