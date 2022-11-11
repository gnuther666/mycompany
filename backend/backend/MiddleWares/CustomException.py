from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exception, content):
    response = exception_handler(exception, content)
    if response is None:
        response = Response()
    response.status_code = 500
    msg = '服务器异常'
    if isinstance(exception, list):
        extern_msg = exception.args[0] if len(exception.args) >= 1 else ''
    else:
        extern_msg = str(exception)
    response.exception = exception
    response.data = {'msg': ':'.join([msg, extern_msg])}
    return response
