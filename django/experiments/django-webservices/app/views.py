from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from app.models import Usuario
from app.forms import UsuarioForm
import os
from os.path import join,realpath
from django.conf import settings

def home(request):
	usuarios=Usuario.objects.all()
	# return render(request, 'index.html', {'usuarios': usuarios,})
	return render_to_response('index.html', {'usuarios': usuarios}, context_instance=RequestContext(request))

def registrar(request):
	if request.method == "POST":
		formulario = UsuarioForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/')

	else:
		formulario=UsuarioForm()

	return render(request, 'nuevo.html', {'formulario': formulario,})

# def eliminar(request):
# 	id_usuario = request.GET.get('usuario', '')
# 	usuario=Usuario.objects.get(pk=id_usuario)
# 	usuario.delete()
# 	return HttpResponseRedirect('/')

def eliminar(request, id_usuario):
	usuario=Usuario.objects.get(pk=id_usuario)
	usuario.delete()
	return HttpResponseRedirect('/')

def editar(request, id_usuario):
# def editar(request):
# 	id_usuario = request.GET.get('usuario', '')
#agregar esto en index en el link editar <a href="{% url 'editar' %}?usuario={{usuario.id}}" class="btn btn-small">Editar</a>
#en las urls: url(r'^editar/$', 'app.views.editar', name='editar'),
	usuario=Usuario.objects.get(pk=id_usuario)
	
	antes=usuario.imagen.name
	nombre=str(antes)
	nombre=nombre[4:]

	if request.method == "POST":
		formulario = UsuarioForm(request.POST, request.FILES, instance = usuario)
		if formulario.is_valid():
			formulario.save()
			if antes!=usuario.imagen:
				print "==============================================="
				print "ELIMINANDO"
				#os.remove(str(img_a))
				os.remove(realpath(join(settings.PROJECT_PATH, 'media/img/' + nombre)))
				print "==============================================="
			return HttpResponseRedirect('/')

	else:
		formulario=UsuarioForm(instance = usuario)

	return render(request, 'editar.html', {'formulario': formulario,})