from django.urls import path

from user.views import AdvertisersView, LoginView

urlpatterns = [
    path('advertisers/', AdvertisersView.as_view()),
    path('login/', LoginView.as_view())
]
