from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from youtube_search import youtube_search
from forms import NameForm

def index(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
	search = request.POST['search']
	id = request.POST.get('playlistID', 'PLwDI47x9eHsFO3r9TxGovXpWbLwDhKcSC')
	template = loader.get_template('addVideo/index.html')
	context = youtube_search(search)
	return HttpResponse(template.render({'context':context, 'id':id}))