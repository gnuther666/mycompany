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