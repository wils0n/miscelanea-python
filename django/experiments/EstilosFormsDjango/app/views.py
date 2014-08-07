# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from app.forms import contacto
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

@csrf_exempt
def procesarFomulario(request):
    valid=False
    if request.method == 'POST': # If the form has been submitted...
        form = contacto(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            valid=True
            email=form.cleaned_data['Email']
            nombre=form.cleaned_data['Nombre']
            titulo=form.cleaned_data['Titulo']
            mensaje=form.cleaned_data['Mensaje']
            print email
            print nombre
            print titulo
            print mensaje
        else:
            print "no es valido, algun campo no se lleno o no es valido"
    return render_to_response('contacto.html',{'form':contacto,'valid':valid},context_instance=RequestContext(request))
