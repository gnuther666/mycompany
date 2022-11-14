from django.utils.deprecation import MiddlewareMixin

import logging

logger = logging.getLogger('company1')


class BeforePrint(MiddlewareMixin):
    def process_request(self, request):
        logger.info('收到请求:' + str(request))

    def process_response(self, request, response):
        logger.info('处理结束:' + str(response))
        return response
