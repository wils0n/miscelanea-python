__author__ = 'wilson'

from django import forms

class contacto(forms.Form):
    Email=forms.EmailField()
    Nombre=forms.CharField(widget=forms.TextInput)
    Titulo=forms.CharField(widget=forms.TextInput)
    Mensaje=forms.CharField(widget=forms.Textarea)