#-*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import RedirectView

from common import views

urlpatterns = [
	
    url(r'^login/$', views.login_page),  
]