# __author__ = 'namibox'
from rest_framework import serializers
from django.contrib.auth.models import User

CDN_DOMIAN = 'https://r.namibox.com/'


class UserSerializer(serializers.ModelSerializer):

    is_active = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login', 'is_superuser', 'first_name', 'is_active')

    def get_is_active(self, obj):
        return 'yes' if obj.is_active else 'no'

