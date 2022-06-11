from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  path('logout', views.logout, name='logout'),
  re_path('register', views.register, name='register'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.myprofile, name='myprofile'),
  re_path(r'^userprofile/(?P<username>\w{0,50}/$)', views.userprofile, name='userprofile'),
  re_path(r'^profile/(?P<username>\w{0,50})/edit/$', views.editprofile, name='editprofile'),
  re_path(r'^profile/(?P<username>\w{0,50})/settings/$', views.settings, name='settings'),
  re_path(r'^project/add/$', views.addportfolio, name='addportfolio'),
  # re_path(r'^project/(?P<username>\w{0,50})/add/$', views.addportfolio, name='addportfolio'),
  # re_path(r'^project/<id>(\d+)/comment/$', views.AddComment, name="AddComment"),
  re_path(r'^search-results/$', views.search, name="search_results")


]