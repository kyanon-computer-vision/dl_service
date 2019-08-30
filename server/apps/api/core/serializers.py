from rest_framework import serializers as sz
from apps.api.authentication.models import User

class UserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')