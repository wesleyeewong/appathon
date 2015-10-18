from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from youtube_search import youtube_search

def index(request):
	template = loader.get_template('addVideo/index.html')
	context = youtube_search("perry")
	return HttpResponse(template.render({'context':context}))