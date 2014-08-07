from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField()
	imagen = models.ImageField(upload_to='img')
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre
