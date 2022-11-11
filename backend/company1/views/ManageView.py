from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from company1.serializer.ManageSerializer import TaskUserTypeSerializer, UserSerializer, MenuConfigSerializer
from company1.models.ManageModel import TaskUserTypeModel, MenuConfigModel
from django.contrib.auth.models import User
from unit.CommonRequest import PageQuery
from django.core.exceptions import BadRequest
from django.forms.models import model_to_dict


class TaskUserTypeSet(viewsets.ModelViewSet):
    queryset = TaskUserTypeModel.objects.all()
    serializer_class = TaskUserTypeSerializer


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    custom_user_field = ['id', 'is_superuser', 'username',
                       'first_name', 'last_name', 'email',
                       'is_staff', 'is_active', 'groups',
                       'user_permissions']
    @action(methods=['get'], detail=False, url_path='user_list')
    def user_list(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        obj = PageQuery(request=request)
        obj.set_field_filter(['id', 'username'])
        data = obj.get_data(response.data)
        return Response(data=data)

    @action(methods=['get'], detail=False, url_path='user_detil')
    def user_detail(self, request, *args, **kwargs):
        use_id = request.GET.get('id', None)
        use_data = -1
        if use_id is not None:
            use_data = UserSet.queryset.filter(pk=use_id).first()
        if use_data is None:
            raise BadRequest('无ID或未找到该用户:' + str(use_id))
        return Response(data=model_to_dict(use_data, fields=UserSet.custom_user_field))


    @action(methods=['post'], detail=False, url_path='edit_user')
    def edit_user(self, request, *args, **kwargs):
        use_id = request.GET.get('id', None)
        use_data = -1
        if use_id is not None:
            use_data = UserSet.queryset.filter(pk=use_id).first()
        if use_data is None:
            raise BadRequest('无ID或未找到该用户:' + str(use_id))
        print(dir(use_data.objects))

        return Response(data=model_to_dict(use_data, fields=UserSet.custom_user_field))

class MenuConfigSet(viewsets.ModelViewSet):
    queryset = MenuConfigModel.objects.all()
    serializer_class = MenuConfigSerializer
