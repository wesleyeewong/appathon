from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from show_playlist_songs import show_playlist_songs

def index(request):
	template = loader.get_template('searchVideo/index.html')
	context = RequestContext(request, {
		'nameList': ["kenny","kenny","kenny"],
		})
	context = show_playlist_songs("PLwDI47x9eHsG9Bqj1L0JZaKLyKcssviDj")
	return HttpResponse(template.render({'context':context}))