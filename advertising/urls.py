from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertising.views.ad_views import AdViewSet, AdRedirectView
from advertising.views.advertiser_views import AdvertisersView

router = DefaultRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path('ads/<int:pk>/click/', AdRedirectView.as_view()),
    path('', include(router.urls)),
    path('advertisers/', AdvertisersView.as_view())
]
