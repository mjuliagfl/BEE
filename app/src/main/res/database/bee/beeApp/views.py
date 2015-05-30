from django.shortcuts import render
from beeApp.models import Tag, Badge
import json
from django.core import serializers
from django.http import HttpResponse

format = 'json'

# Create your views here.

#TAG'S VIEW
def add_tag(request, tag_title):
	if not (Tag.objects.filter(title = tag_title)):
		tag = Tag(title = tag_title)
		tag.save()
		return HttpResponse(serializers.serialize(format, [tag]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_tag(request, tag_title):
	tag = (Tag.objects.filter(title = tag_title))
	if tag:
		tag.delete()
		return HttpResponse(serializers.serialize(format, []))
	else:
		return HttpResponse(serializers.serialize(format, [tag]))

def change_title_tag(request, tag_title, new_title):
	tag = (Tag.objects.filter(title = tag_title))
	if tag:
		tag.title = new_title
		tag.save()
		return HttpResponse(serializers.serialize(format, [tag]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_tag(request, tag_title):
	data = serializers.serialize(format, (Tag.objects.filter(title = tag_title)))
	return HttpResponse(data)

def get_all_tags(request):
	data = serializers.serialize(format, Tag.objects.all())
	return HttpResponse(data)


#BADGE'S VIEW

def add_badge(request, badge_name, badge_description, badge_icon):
	if not (Badge.objects.filter(name = badge_name, description = badge_description, icon = badge_icon)):
		badge = Badge(name = badge_name, description = badge_description, icon = badge_icon)
		badge.save()
		return HttpResponse(serializers.serialize(format, [badge]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_badge(request, badge_name):
	badge = (Badge.objects.filter(name = badge_name))
	if badge:
		badge.delete()
		return HttpResponse(serializers.serialize(format, []))
	else:
		return HttpResponse(serializers.serialize(format, [badge]))


def change_name_badge(request, badge_name, new_name):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].name = new_name
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def change_description_badge(request, badge_name, new_description):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].description = new_description
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def change_icon_badge(request, badge_name, new_icon):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].icon = new_icon
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_badge_icon(request, badge_name):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		icon = badge[0].icon
		return HttpResponse(icon)
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_all_badges(request):
	data = serializers.serialize(format, Badge.objects.all())
	return HttpResponse(data)

#POST'S VIEWS

def add_post(request, post_text, post_tags, post_date_hour, post_author):
	if not (Post.objects.filter(text = post_text, tags = post_tags, date_hour = post_date_hour, author = post_author)):
		post = Post(text = post_text, tags = post_tags, date_hour = post_date_hour, author = post_author)
		post.save()
		return HttpResponse(serializers.serialize(format, [post]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_post(request, post_id_p):
	post = Post.objects.get(post_id_p)

	if post:
		ret_post = post[0]
		post[0].delete()
		return HttpResponse(serializers.serialize(format, [ret_post]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def update_post_text(request, post_id_p, post_new_text):
	post = Post.objects.get(post_id_p)

	if post:
		post[0].text = post_new_text
		post[0].save()
		return HttpResponse(serializers.serialize(format, [post]))

	else:
		return HttpResponse(serializers.serialize(format, []))

def update_post_tags(request, post_id_p, post_new_tags):
	post = Post.objects.get(post_id_p)

	if post:
		post[0].tags = post_new_tags
		post[0].save()
		return HttpResponse(serializers.serialize(format, [post]))

	else:
		return HttpResponse(serializers.serialize(format, []))

def get_post_number_likes(request, post_id_p):
	number = Post.post_likes.objects.filter(post_id = post_id_p).count()
	return HttpResponse(number)

def get_post_number_reports(request, post_id_p):
	number = Post.post_reports.objects.filter(post_id = post_id_p).count()
	return HttpResponse(number)

def like_post(request, post_id_p, post_person_liked_id):
	like = Post.post_likes.objects.get(post_id_p, post_person_liked_id)

	if not like:
		post = Posts.objects.get(post_id_p)
		post[0].post_likes.add(post_id_p, post_person_liked_id)
		return HttpResponse(serializers.serialize(format, []))
	else:
		ret_like = like[0]
		like[0].delete()
		return HttpResponse(serializers.serialize(format, [ret_like]))

def report_post(request, post_id_p, post_person_reported_id):
	report = Post.post_reports.objects.get(post_id_p, post_person_reported_id)

	if not report:
		post = Posts.objects.get(post_id_p)
		post[0].post_reports.add(post_id_p, post_person_reported_id)
		return HttpResponse(serializers.serialize(format, []))
	else:
		ret_report = report[0]
		report[0].delete()
		return HttpResponse(serializers.serialize(format, [ret_report]))

def get_all_posts(rquest):
	data = serializers.serialize(format, Post.objects.all())
	return HttpResponse(data)










