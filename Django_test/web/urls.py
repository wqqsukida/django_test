#!/usr/bin/env python
# coding:utf-8
#url路由
from django.conf.urls import url
from django.contrib import admin
from views import add,delete,update,get,Assetlist,Login,Many


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^add/(?P<name>\w*)/$', add),  #将url为add的交给add函数（给表添加一条数据）处理
    url(r'^delete/(?P<name>\w*)/$',delete),#(?P<name>\w*)为正则命名捕获组：匹配到\w*保存到内存里并命名为name,方便后面引用  
    url(r'^update/(?P<id>\d*)/(?P<name>\w*)/$',update),
    url(r'^get/(?P<name>\w*)/$',get),
    
    url(r'^assetlist/$',Assetlist),
    url(r'^login/$',Login),
    url(r'^many/$',Many),
]
