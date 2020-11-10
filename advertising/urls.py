from django.urls import path

from advertising.views import AdvertisersView, AdRedirectView

urlpatterns = [
    path('advertisers/', AdvertisersView.as_view()),
    path('ads/<int:pk>/click/', AdRedirectView.as_view())
]
