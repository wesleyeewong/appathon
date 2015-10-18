from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from list_playlist import ListPlaylist
import json

def index(request):
	template = loader.get_template('playList/index.html')
	#context = RequestContext(request, {
	#	'nameList': ["wesley","kenny","kristy"],
	#	})
	context = ListPlaylist()
	return HttpResponse(template.render({'context': context }))