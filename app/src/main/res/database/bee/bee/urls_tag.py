from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views

urlpatterns = [
    url(r'^add/(?P<tag_title>[\w]+)', views.add_tag),
    url(r'^delete/(?P<tag_title>[\w]+)', views.delete_tag),
    url(r'^(?P<tag_title>[\w]+)', views.get_tag),
    url(r'^update_title/(?P<tag_title>[\w]+)/(?P<new_title>[\w]+)', views.change_title_tag),
    url(r'^$', views.get_all),
]
