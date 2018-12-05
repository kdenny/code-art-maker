from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload_pic/$', views.upload_pic, name="upload_pic"),
    url(r'^homepage/$', views.homepage, name="home"),
    url(r'^images/$', views.ImageList.as_view()),
    url(r'^images/(?P<image_type>[\w\-]+)/$', views.ImageList.as_view()),
    url(r'^projects/$', views.ProjectsList.as_view()),
    url(r'^projects/(?P<status>[\w\-]+)/$', views.ProjectsList.as_view()),
]