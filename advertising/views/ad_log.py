from rest_framework import views
from rest_framework.response import Response

from advertising.models import Ad


class AdLogView(views.APIView):

    def get(self, request, **kwargs):
        hour = int(request.query_params.get('hour', 12))
        ad = Ad.objects.filter(id=self.kwargs.get('pk')).first()
        clicks_count = ad.clicks.filter(time__hour__range=(hour, hour+1)).count()
        views_count = ad.views.filter(time__hour__range=(hour, hour+1)).count()
        return Response(data={
            'clicks': clicks_count, 'views': views_count,
        })

