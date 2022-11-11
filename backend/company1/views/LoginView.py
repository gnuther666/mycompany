import re
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import viewsets
from company1.serializer.ManageSerializer import LoginSerializer
User = get_user_model()


class LoginView(viewsets.ModelViewSet):
    """
    登陆视图，用户名与密码匹配返回token
    """
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            # 获取前台穿的usr和pwd字段
            usr = request.data.get("usr")
            pwd = request.data.get("pwd")
        except KeyError:
            return Response(data_status=10002, data_msg="请求数据非法")
        if re.match(r"1[35678]\d{9}", usr):
            # 正则匹配手机号
            user = User.objects.filter(phone=usr).first()
        elif re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', usr):
            # 正则匹配邮箱
            user = User.objects.filter(email=usr).first()
        else:
            # 用户名
            user = User.objects.filter(username=usr).first()
        if not user:
            return Response(data_status=10002, data_msg="该用户未注册")
        if user.is_active == 0:
            return Response(data_status=10002, data_msg="用户被禁用")
        if not check_password(pwd, user.password):
            return Response(data_status=10002, data_msg="用户名或密码错误")

        # 调用第三方的JWT_PAYLOAD_HANDLER和JWT_ENCODE_HANDLER，这里也可以自定义该方法
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        # 通过user解析出payload
        payload = jwt_payload_handler(user)
        # 通过payload生成token
        token = jwt_encode_handler(payload)
        return Response(token=token, results={"user": user.username})
