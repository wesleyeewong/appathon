from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from show_playlist_songs import show_playlist_songs

def index(request):
	id = request.GET.get('id')
	template = loader.get_template('searchVideo/index.html')
	context = show_playlist_songs(id.encode())
	return HttpResponse(template.render({'context':context}))
