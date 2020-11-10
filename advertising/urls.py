from django.urls import path

from advertising.views import AdvertisersView, AdRedirectView, AdCreateView

urlpatterns = [
    path('advertisers/', AdvertisersView.as_view()),
    path('ads/<int:pk>/click/', AdRedirectView.as_view()),
    path('ads/create_form/', AdCreateView.as_view())
]
