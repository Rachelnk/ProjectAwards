from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.login, name='login'),
  re_path('register', views.register, name='register'),

]