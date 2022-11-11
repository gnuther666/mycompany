from company1.models.ManageModel import TaskUserTypeModel, MenuConfigModel
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskUserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskUserTypeModel
        fields = ['id', 'UserEn', 'UserCn']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_superuser', 'first_name', 'last_name', 'email', 'is_staff', 'is_active'] # '__all__'

class MenuConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuConfigModel
        fields = ['id', 'ParentId', 'MenuEn', 'MenuCn', 'IsNeedSuper']


class LoginSerializer(serializers.ModelSerializer):
    # 设置自定义的反序列化字段usr，pwd
    usr = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'usr', 'pwd']
        extra_kwargs = {
            "username": {
                "read_only": True
            },
            "email": {
                "read_only": True
            },
            "phone": {
                "read_only": True
            }
        }
