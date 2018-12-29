from django.utils.deprecation import MiddlewareMixin
from django.contrib import auth
from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect 
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

CALLBACK_URI = ['/', '/system/login/']
 
class CheckRequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path not in CALLBACK_URI:
             # 如果未登录
            if isinstance(request.user, auth.models.AnonymousUser):
                return redirect('/')

    def process_response(self, request, response):
        user = request.user
        response['Access-Control-Allow-Credentials'] = True
        response['Access-Control-Allow-Headers'] = 'Content-Type, authorization'
        response['Access-Control-Allow-Methods'] = "GET, POST, PUT, DELETE, OPTIONS, HEAD"
        response['Access-Control-Allow-Origin'] = '*'
        # 'Access-Control-Allow-Headers': ‘Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With'
        if request.path not in CALLBACK_URI:
            # 如果已经登录
            if not isinstance(user, auth.models.AnonymousUser):
                context = {
                    "request": request,
                    "view": self,
                }
                token = request.COOKIES.get("jwt_token")
                kwargs = {
                    'context': context,
                    'data': {
                        'token': token
                    }
                }
                serializer = VerifyJSONWebTokenSerializer(**kwargs)
                is_valid = serializer.is_valid()
                if not is_valid:
                    # token 过期
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)

                    next = request.GET.get("next")
                    if next:
                        response = redirect(next)
                    # unionid 写入 cookie, 然后到绑定页面
                    response.set_cookie('jwt_token', token, max_age=api_settings.JWT_EXPIRATION_DELTA.total_seconds())
                    return response
        return response