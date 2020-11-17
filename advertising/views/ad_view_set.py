from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response

from DBDjango.custom_viewsets import ListCreateRetrieveViewSet
from advertising.models import Ad
from advertising.views.logs.annotators import annotate_general, annotate_hour_filtered
from advertising.serializers import AdSerializer


class AdViewSet(ListCreateRetrieveViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @staticmethod
    def annotate_logs(request, query):
        query, fields = annotate_general(query, ['id'])
        if request.query_params.get('hour', None):
            hour = int(request.query_params.get('hour'))
            return annotate_hour_filtered(query, fields, [], hour)
        else:
            return query.values(*fields)

    @action(detail=True, url_path='log', url_name='log')
    def log(self, request, pk=None):
        self.queryset.filter(pk=9).values()
        return Response(data=self.annotate_logs(request, self.queryset.filter(pk=pk)))

    @action(detail=False, url_path='log', url_name='log')
    def logs(self, request):
        return Response(data=self.annotate_logs(request, self.queryset))