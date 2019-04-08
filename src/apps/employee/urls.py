# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.employee import views

urlpatterns = [
    #企业招聘信息
    url(r'^job$',views.get_job),
]