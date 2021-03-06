from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  re_path('logout', views.logoutUser, name='logout'),
  re_path('register', views.register, name='register'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.myprofile, name='myprofile'),
  re_path(r'^userprofile/(?P<username>\w{0,50}/$)', views.userprofile, name='userprofile'),
  re_path(r'^profile/(?P<username>\w{0,50})/edit/$', views.editprofile, name='editprofile'),
  re_path(r'^profile/(?P<username>\w{0,50})/settings/$', views.settings, name='settings'),
  re_path(r'^project/add/$', views.addportfolio, name='addproject'),
  re_path(r'^profile/(?P<username>\w{0,50})/project/$', views.myportfolio, name="myproject"),
  re_path(r'^search-results/$', views.search, name="search_results"),
  # re_path(r'^project/(?P<title>\w{0,50})\S/details/$', views.portfoliodetails, name="project_details"),
  path('project/<str:title>/details', views.portfoliodetails, name="project_details"),
  path('profile/<str:username>/project/<str:title>/delete', views.deleteportfolio, name="deleteproject"),
  path('profile/<str:username>/project/<int:id>/edit', views.editportfolio, name="EditPortfolio"),
  path('portfolio/<str:title>/rate', views.portfoliorating, name="projectrating"),
  re_path(r'^api/profiles/$', views.ProfileList.as_view()),
  re_path(r'^api/projects/$', views.PortfolioList.as_view())


]