# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.get_activity_info import views

urlpatterns = [
    #基础信息获取
    url(r'^pai$', views.post_activity_info),
    url(r'^gai/(?P<name>\w+)/(?P<time>\w+)/$', views.get_activity_info),
    url(r'^link$', views.activity),
    url(r'^help$', views.get_help_info),
    url(r'^success$', views.data_post),
    url(r'^test$', views.test)
]