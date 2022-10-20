from rest_framework.views import exception_handler

from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger('company1')

def custom_exception_handler(exc, context) -> Response:
    '''
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response 响应对象
    '''
    response = exception_handler(exc, context)

    if response is None:
        '''2个情况，要么程序未出错，或者rest_framework不识别'''
        view = context['view']
        if isinstance(exc, DatabaseError):
            logger.error('[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误,请联系客服工作人员'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response