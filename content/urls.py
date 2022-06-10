from content import views
from django.urls import re_path, path

urlpattern = [
  path('', views, name='index'),
  path('login', views, name='login'),
  re_path('register', views, name='register'),

]