from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer,UserLinkSerializer, GroupSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import (NotFound, ParseError, PermissionDenied)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as r_filters
from rest_framework import status as HTTPStatus
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    # """
    # 这一viewset提供了`list`, `create`, `retrieve`, `update` 和 `destroy`
    # """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


    filter_backends = (r_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id',)
    ordering_fields = ('id', 'date_joined',)


    permission_classes_by_action = {
        'default':[AllowAny],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update':[IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes_by_action['default']]

    # def get_object(self):
    #     # 重写父类方法

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        pass
        return Response(advertise, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        pass


    @detail_route(methods=['post'])
    def login(self, request):
        pass
        return Response({'settings': settings}, status=status.HTTP_200_OK)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer