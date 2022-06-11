from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  re_path('register', views.register, name='register'),
  re_path(r'^myprofile/(?P<username>\w{0,50})/$', views.myprofile, name='myprofile'),
  re_path(r'^userprofile/(?P<username>\w{0.50}/$)', views.userprofile, name='userprofile'),
  re_path(r'^userprofile/(?P<username>\w{0.50})/edit/$', views.editprofile, name='editprofile'),

]