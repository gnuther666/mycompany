from django.utils.deprecation import MiddlewareMixin


class BeforePrint(MiddlewareMixin):
    def process_request(self, request):
        print(request.get_host())
        print(request.headers)
        # print(dir(request.get_port()))

    def process_response(self,request,response):
        print('处理结束:', response)
        return response
