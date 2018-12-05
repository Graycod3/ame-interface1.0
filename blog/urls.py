
from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('post/new/', views.post_L, name='post_L'),
    path('post/new/staticE', views.post_new, name='post_new'),
    path('post/new/dhcpE', views.post_list_four, name='post_list_Eth'),
    #path wifi
    path('post/news/', views.post_list_two, name='post_list_two'),
    path('post/new/dhcp', views.post_list_four, name='post_list_four'),
    path('post/new/static', views.post_list_three,name='post_list_three'),
]
