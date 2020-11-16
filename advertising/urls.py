from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertising.views import AdViewSet, AdRedirectView

router = DefaultRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path('ads/<int:pk>/click/', AdRedirectView.as_view()),
    path('', include(router.urls))
]
