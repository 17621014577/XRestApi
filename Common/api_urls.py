from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import api


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', api.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
