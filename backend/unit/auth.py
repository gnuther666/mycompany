import jwt
from django.contrib.auth import get_user_model
from rest_framework.authentication import get_authorization_header
from rest_framework_jwt.authentication import jwt_decode_handler, BaseJSONWebTokenAuthentication, \
    jwt_get_username_from_payload
from rest_framework import exceptions

User = get_user_model()  # 获取用户模型


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    keyword = "JWT"

    def authenticate(self, request):
        # 获取请求头字符串，分割成列表
        try:
            auth = get_authorization_header(request).split()
            if not auth:
                msg = "未获取到Authorization请求头"
                raise exceptions.AuthenticationFailed(msg)
            if auth[0].lower() != self.keyword.lower().encode():
                msg = "Authorization请求头中认证方式错误"
                raise exceptions.AuthenticationFailed(msg)
            if len(auth) == 1:
                msg = "非法Authorization请求头"
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                raise exceptions.AuthenticationFailed({"message": "无效的授权头。凭据字符串''不应包含空格"})
            try:
                jwt_token = auth[1]
                payload = jwt_decode_handler(jwt_token)
            except jwt.ExpiredSignature:
                msg = 'token已失效'
                raise exceptions.AuthenticationFailed(msg)
            except jwt.DecodeError:
                msg = '签名解析失败'
                raise exceptions.AuthenticationFailed(msg)
            except jwt.InvalidTokenError:
                raise exceptions.AuthenticationFailed()

            user = self.authenticate_credentials(payload)
            print('正常退出2')
            return user, jwt_token
        except Exception as e:
            print('异常啦2:authenticate_credentials', str(e))
            raise e

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()
        username = jwt_get_username_from_payload(payload)
        try:
            if not username:
                msg = _('Invalid payload.')
                raise exceptions.AuthenticationFailed(msg)

            try:
                user = User.objects.get_by_natural_key(username)
            except User.DoesNotExist:
                msg = '用户不存在'
                raise exceptions.AuthenticationFailed(msg)

            if not user.is_active:
                msg = '用户已禁用'
                raise exceptions.AuthenticationFailed(msg)
            print('正常退出1')
            return user
        except Exception as e:
            print('异常啦1:authenticate_credentials', str(e))
            raise e
