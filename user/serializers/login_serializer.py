from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_403_FORBIDDEN


class LoginSerializer(AuthTokenSerializer):

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    def validate(self, data):
        print(1)
        username, password = data.get('username', ''), data.get('password', '')
        user = get_object_or_404(User.objects.all(), username=username)

        print(2)

        if not check_password(password, user.password):
            raise ValidationError(
                '~WRONG PASSWORD~', code=HTTP_403_FORBIDDEN
            )
        print(3)
        data['user'] = user
        return data
