from rest_framework import serializers

from advertising.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image_url', 'link', 'advertiser', 'create_time']
        extra_kwargs = {'create_time': {'read_only': True}}