from django.urls import path

from advertising.views import AdvertisersView, AdRedirectView, AdCreateView, AdLogView, AdLogsView

urlpatterns = [
    path('advertisers/', AdvertisersView.as_view()),
    path('ads/<int:pk>/click/', AdRedirectView.as_view()),
    path('ads/create_form/', AdCreateView.as_view()),
    path('ads/log/', AdLogView.as_view())
]
