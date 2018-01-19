#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: urls.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-19 09:53:17
# Last Modified: 2018-01-19 09:53:19
#***********************************************

__author__ = 'Benson'

from blog import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.Index, name='index'),
    url(r'^about/$', views.About, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^link/$', views.Link, name='link'),
    url(r'^message$', views.Message, name='message'),
    url(r'^article/(?P<pk>\d+)/$', views.Articles, name='article'),
    url(r'^get_comment/$', views.GetComment, name='get_comment'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),

]
