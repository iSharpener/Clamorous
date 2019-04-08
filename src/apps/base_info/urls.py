# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.base_info import views

urlpatterns = [
    #基础信息获取
    url(r'^gbi$',views.get_base_info)
]