from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views

urlpatterns = [
	url(r'^add/(?P<post_text>[\w]+)/(?P<comment_tags>[\w]+)/(?P<post_date_hour>[0-3][0-9]\\[0-1][0-9]\\[0-2][0-9][0-9][0-9]\:[0-2][0-9]\:[0-5][0-9]+)/(?P<post_author>[\w])', views.add_post),
	url(r'^delete/(?P<post_id_p>[0-9]+)', views.delete_post),
	url(r'^update_text/(?P<post_id_p>[0-9]+)/(?P<post_new_text>[\w]+)', views.update_post_text),
	url(r'^update_tags/(?P<post_id_p>[0-9]+)/(?P<post_new_tags>[\w]+)', views.update_post_tags),
	url(r'^get_number_likes/(?P<post_id_p>[0-9]+)', views.get_post_number_likes),
	url(r'^get_number_reports/(?P<post_id_p>[0-9]+)', views.get_post_number_reports),
	url(r'^like/(?P<post_id_p>)[0-9]+/(?P<post_person_liked_id>[\w]+)', views.like_post),
	url(r'^report/(?P<post_id_p>)[0-9]+/(?P<post_person_reported_id>[\w]+)', views.report_post),
	url(r'^$', views.get_all)
]
