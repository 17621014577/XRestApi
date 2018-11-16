# __author__ = 'namibox'
from rest_framework import serializers
from django.contrib.auth.models import User, Group



class UserLinkSerializer(serializers.HyperlinkedModelSerializer):
    # HyperlinkedModelSerializer 类与 ModelSerializer 类相似，只不过它使用超链接来表示关系而不是主键。

    # 默认情况下，序列化器将包含一个 url 字段而不是主键字段。
    class Meta:
        model = User
        fields = ('url','username', 'email', 'last_login', 'is_superuser', 'first_name', 'is_active')

class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'is_superuser', 'first_name', 'is_active')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')