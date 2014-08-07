# Create your views here.
# coding=utf-8
from os.path import join, realpath
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import django.utils.simplejson as json

@csrf_exempt
def home(request):
	json_data = request.read()
	#json_data = json.dumps({"key1": 1, "key2": 2})
	# json_data contains the data uploaded in request
	print "=================="
	print "recibiendo la data de un request"
	print json_data
	print type(json_data)
	data = json.loads(json_data)
	print "cargando la data de un request"
	print data
	print type(data)
	print data.keys()
	return HttpResponse(json_data, content_type = "application/json")