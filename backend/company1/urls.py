from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from company1.views.basetest import test_basehttp_response
from company1.views.ManageView import TaskUserTypeSet, UserSet, MenuConfigSet
from company1.views.LoginView import LoginView
router = routers.DefaultRouter()
router.register(r'TaskUserType', TaskUserTypeSet)
router.register(r'User', UserSet)
router.register(r'MenuConfig', MenuConfigSet)
router.register(r'Login', LoginView)

urlpatterns = [
    path('test_basehttp_response/', test_basehttp_response),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
]