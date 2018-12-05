
from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name = 'post_list'),
   #1st one works
    path('post/new/', views.post_L, name='post_L'),
	#2nd one works    
    path('post/new/static', views.post_new, name='post_new'),
    #path('post/new/dhcp', views.post_new, name='post_dhcp')
]
