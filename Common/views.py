# Create your views here.

import json
import datetime
from django.shortcuts import HttpResponse, render, redirect
from migrate_apps.migrate_utils import is_ajax
from django.contrib import auth

from django.contrib import messages
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def login_page(request):

    if request.method == 'GET':
        return render(request, 'common/templates/login.html')
    if request.method == 'POST':
        # try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next', None)

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, '用户名密码不匹配')
            return redirect('/')
        auth.login(request, user)
        return redirect('/')

