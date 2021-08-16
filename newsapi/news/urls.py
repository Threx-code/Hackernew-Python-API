from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.StoryList.as_view(), name=views.StoryList.name),
    url('^stories/$', views.StoryList.as_view(), name=views.StoryList.name),
    url(r'^stories(?P<pk>[0-9]+)/$', views.StoryDetail.as_view(), name=views.StoryDetail.name),
    url(r'^comments/$', views.CommentList.as_view(), name=views.CommentList.name),
    url(r'^comments(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name=views.CommentDetail.name),
]
