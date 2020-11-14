from rest_framework import views
from rest_framework.response import Response

from advertising.models import Ad
from advertising.views.logs.annotators import annotate_general, annotate_hour_filtered


class AdLogView(views.APIView):

    def get(self, request):
        query, fields = annotate_general(Ad.objects.all(), ['id'])

        if request.query_params.get('hour', None):
            hour = int(request.query_params.get('hour'))
            query, fields = annotate_hour_filtered(query, fields, hour)

        if request.query_params.get('id', None):
            query = query.filter(id=request.query_params['id'])

        return Response(data=query.values(*fields))
