from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from company1.serializer.ManageSerializer import TaskUserTypeSerializer, UserSerializer, MenuConfigSerializer
from company1.models.ManageModel import TaskUserTypeModel, MenuConfigModel
from django.contrib.auth.models import User
from unit.CommonRequest import PageQuery

class TaskUserTypeSet(viewsets.ModelViewSet):
    queryset = TaskUserTypeModel.objects.all()
    serializer_class = TaskUserTypeSerializer

class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False, url_path='user_list')
    def user_list(self, request, *args, **kwargs):
        response = self.list(request, * args, **kwargs)
        obj = PageQuery(request=request)
        obj.set_field_filter(['id', 'username'])
        data = obj.get_data(response.data)
        return Response(data=data)

class MenuConfigSet(viewsets.ModelViewSet):
    queryset = MenuConfigModel.objects.all()
    serializer_class = MenuConfigSerializer