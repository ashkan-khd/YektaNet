from rest_framework import serializers

from advertising.models import Ad


class AdSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['advertiser'] = self.context['request'].user.advertiser
        return data

    class Meta:
        model = Ad
        fields = ['id', 'title', 'image_url', 'link', 'advertiser', 'created']
        extra_kwargs = {'advertiser': {'read_only': True}}
