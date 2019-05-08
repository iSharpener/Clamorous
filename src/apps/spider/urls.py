# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.spider import views

urlpatterns = [
    #科研成果
    url(r'^research$',views.get_research),
    #研究生校园招聘信息
    url(r'^zhaopin$',views.zhaopin),
    url(r'^dangjian$', views.dangjian),
    url(r'^zhaopin_detail$',views.zhaopin_detail),
    url(r'^get_research_detail$',views.get_research_detail),
    url(r'^zhaopin_detail',views.zhaopin_detail),
    url(r'^employment_counsel',views.employment_counsel),
    url(r'^zhidao_detail',views.zhidao_detail),
]