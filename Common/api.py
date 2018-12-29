from django.contrib.auth.models import User, Group
from django.contrib import auth
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import (NotFound, ParseError, PermissionDenied)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.settings import api_settings
from rest_framework import filters
from django_filters import rest_framework as r_filters
from rest_framework import status as HTTPStatus
from django.shortcuts import get_object_or_404
from django.db.models import Max
from .serializers import UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(viewsets.ModelViewSet):
    # """
    # 这一viewset提供了`list`, `create`, `retrieve`, `update` 和 `destroy`
    # """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer 
    permission_classes = (AllowAny, )

    filter_backends = (r_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id',)
    ordering_fields = ('id', 'date_joined',)

    @list_route(methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'token': token, 'user_id': user.id}, status=status.HTTP_200_OK)
        raise PermissionDenied(detail='用户名密码不正确')

    def list(self, request):
        return NotFound(detail='不提供该接口')