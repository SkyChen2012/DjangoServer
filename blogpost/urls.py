from django.conf.urls import include, url  
from blogpost.views import *  
  
urlpatterns = [ 
	# blog_1  
	
    url(r'^$',index),
    url(r'^blog/(?P<slug>[^\.]+).html', view_post, name='view_blog_post'),  
]