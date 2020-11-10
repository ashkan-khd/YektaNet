from django.views.generic import CreateView
from advertising.models import Ad


class AdCreateView(CreateView):
    template_name = 'ad_form.html'
    model = Ad
    fields = ['advertiser', 'image_url', 'title', 'link']

    def get_success_url(self):
        return '/advertising/advertisers/'