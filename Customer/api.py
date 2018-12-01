from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, NewsSerializer
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
from .models import WebSiteNews, NewsCategory
from django.db.models import Max

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(viewsets.ModelViewSet):
    # """
    # 这一viewset提供了`list`, `create`, `retrieve`, `update` 和 `destroy`
    # """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id',)
    ordering_fields = ('id', 'date_joined',)
    # http://localhost:8000/api/v1/users/?id=1&ordering=-id

    # permission_classes_by_action = {
    #     'default':[AllowAny],
    #     'list': [AllowAny],
    #     'retrieve': [AllowAny],
    #     'update':[IsAuthenticated],
    # }

    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action`
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes_by_action['default']]

    # # def list(self, request, *args, **kwargs):
    #     # pass

    # def retrieve(self, request, pk=None):
    #     user = User.objects.get(pk=pk)
    #     serializer = self.serializer_class(user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def login(self, request):
        user = User.objects.get(id=1)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token, 'user_id': user.id}, status=status.HTTP_200_OK)


class NewsViewSet(viewsets.ModelViewSet):
    """
    官网新闻
    """
    queryset = WebSiteNews.objects.all()
    serializer_class = NewsSerializer  
    permission_classes = (IsAuthenticated, )
    
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('category_id',)
    ordering_fields = ('id', 'top', 'sort', 'hits')

    @detail_route(methods=['patch'])
    def publish_news(self, request, pk):
        status = request.GET.get('status')
        news = WebSiteNews.objects.get(id=pk)
        news.status=status
        news.save()
        return Response({'message':'操作成功'}) 

    @detail_route(methods=['get'])
    def set_top(self, request, pk):
        news = WebSiteNews.objects.get(id=pk)
        top = WebSiteNews.objects.all().aggregate(Max('top'))
        news.top = top['top__max'] + 1
        news.save()
        return Response({'message':'操作成功'}) 

    # @list_route(methods=['get'])
    # def get_list(self, request):
    #     queryset = self.queryset
    #     serializer = NewsSerializer(queryset, many=True)
    #     return Response(serializer.data)     
            
    def destroy(self, request, pk):
        news = WebSiteNews.objects.get(id=pk)
        news.deleted = True
        news.save()
        return Response({'message':'操作成功'}) 

    def retrieve(self, request, pk=None):
        news = WebSiteNews.objects.get(id=pk)
        news.hits += 1
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)     

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'操作成功'}) 