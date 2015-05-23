from django.shortcuts import render
from beeApp.models import Tag
import json
from django.core import serializers
from django.http import HttpResponse

format = 'json'

# Create your views here.
def add_tag(request, tag_title):
	if not (Tag.objects.filter(title = tag_title)):
		tag = Tag(title = tag_title)
		tag.save()
		return HttpResponse("SUCCESS")
	else:
		return HttpResponse("FAIL")

def delete_tag(request, tag_title):
	tag = (Tag.objects.filter(title = tag_title))
	if tag:
		tag.delete()
		return HttpResponse("SUCCESS")
	else:
		return HttpResponse("FAIL")

def get_tag(request, tag_title):
	data = serializers.serialize(format, (Tag.objects.filter(title = tag_title)))
	return HttpResponse(data)

def get_all(request):
	data = serializers.serialize(format, Tag.objects.all())
	return HttpResponse(data)










