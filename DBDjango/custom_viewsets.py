from rest_framework import mixins, viewsets


class ListCreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    pass
