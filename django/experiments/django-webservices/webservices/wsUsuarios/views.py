from django.http import HttpResponse
from app.models import Usuario
from django.core import serializers
from django.utils import simplejson

def wsUsuarios_view(request):
	#data = serializers.serialize('json', Usuario.objects.filter(status=True))
	#data = serializers.serialize('json', Usuario.objects.filter(status=True), fields=('nombres','apellidos', 'edad'))
	json = simplejson.dumps( [{'nombre': i.nombre, 'apellidos': i.apellidos} for i in Usuario.objects.all()] )
	return HttpResponse(json, mimetype = 'application/json')