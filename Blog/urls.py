from django.conf.urls import include, url  
from Blog.views import *  
  
urlpatterns = [  
	# blog_2
	
    url(r'^$',get_blogs),
    url(r'^blog/(\d+)/$',get_details ,name='blog_get_detail'),
]