from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from show_playlist_songs import show_playlist_songs
from add_video import add_song

def index(request):
	id = request.GET.get('id')
	template = loader.get_template('searchVideo/index.html')
	context = show_playlist_songs(id.encode())
	return HttpResponse(template.render({'context':context, 'id':id}))


def add(request):
	playlistID = request.GET.get('playlistID')
	videoID = request.GET.get('videoID')
	template = loader.get_template('searchVideo/index.html')
	result = add_song(playlistID, videoID)
	print result
	context = show_playlist_songs(playlistID.encode())
	return HttpResponse(template.render({'context':context, 'id':playlistID}))