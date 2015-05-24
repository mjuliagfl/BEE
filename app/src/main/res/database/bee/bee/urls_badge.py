from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views

urlpatterns = [
    url(r'^add/(?P<badge_name>[\w]+)/(?P<badge_description>[\w]+)/(?P<badge_icon>[\w]+)', views.add_badge),
    url(r'^delete/(?P<badge_name>[\w]+)', views.delete_badge),
    url(r'^update_name/(?P<badge_name>[\w]+)/(?P<new_name>[\w]+)', views.change_name_badge),
    url(r'^update_description/(?P<badge_name>[\w]+)/(?P<new_description>[\w]+)', views.change_description_badge),
    url(r'^update_icon/(?P<badge_name>[\w]+)/(?P<new_icon>[\w]+.[\w]+)', views.change_icon_badge),
    url(r'^icon/(?P<badge_name>[\w]+)', views.get_badge_icon),
    url(r'^$', views.get_all)
]
