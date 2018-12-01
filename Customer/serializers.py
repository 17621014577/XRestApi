# __author__ = 'namibox'
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NewsCategory, WebSiteNews

CDN_DOMIAN = 'https://r.namibox.com/'


class UserSerializer(serializers.ModelSerializer):

    is_active = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login', 'is_superuser', 'first_name', 'is_active')

    def get_is_active(self, obj):
        return 'yes' if obj.is_active else 'no'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsCategory
        fields = ("category_name",)


class NewsSerializer(serializers.ModelSerializer):

    # status = serializers.SerializerMethodField(read_only=True)
    cover_image = serializers.SerializerMethodField(read_only=True)
    category_name = serializers.SerializerMethodField(read_only=True)
    hits = serializers.IntegerField()

    class Meta:
        model = WebSiteNews
        fields = ("id", "title", "content", "category_name", "cover_image",
                  "publish_time", "hits")
        depth = 1

    def get_category_name(self, obj):
        return obj.category.category_name

    def get_cover_image(self, obj):
        return CDN_DOMIAN + (str(obj.cover_image))
