from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('searchVideo/index.html')
	context = RequestContext(request, {
		'nameList': ["wesley","kenny","kristy"],
		})
	return HttpResponse(template.render(context))