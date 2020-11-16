from rest_framework import serializers

from advertising.models import Ad


class AdSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['advertiser'] = self.context['request'].user.advertiser
        return data

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        return ad

    class Meta:
        model = Ad
        fields = ['id', 'title', 'image_url', 'link', 'advertiser', 'create_time']
        extra_kwargs = {'advertiser': {'read_only': True}}
