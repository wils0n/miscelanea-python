from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import json

def home(request):
	return render_to_response('index.html', {'nombre':'Hola Mundo'}, context_instance=RequestContext(request))

def cargar_contenido(request, id):
	return HttpResponse(
		json.dumps({'nombre': 'Hola Mundo', 'descripcion': 'print "Hola Mundo"'}), 
		content_type="application/json; charset=uft8"
		)