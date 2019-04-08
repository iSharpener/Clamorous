# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.commu_info import views

urlpatterns = [
    #登录模块
    url(r'^login$',views.LoginView.as_view()),
    #下线模块
    url(r'^logout$',views.LogoutView.as_view())
]