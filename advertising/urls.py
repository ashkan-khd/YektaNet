from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertising.views import AdvertisersView, AdRedirectView
from advertising.views.ad_view import AdViewSet

router = DefaultRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path('advertisers/', AdvertisersView.as_view()),
    path('ads/<int:pk>/click/', AdRedirectView.as_view()),
    path('', include(router.urls))
]
