# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.wechat import views
# from apps.wechat import AuthView, GetInfoView

urlpatterns = [
    url(r'^$', views.weixin_main),
    # url(r'^auth/$', AuthView.as_view()),
    # url(r'^index$', GetInfoView.as_view()),
]
