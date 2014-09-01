##1.1 La importancia de hacer tu código legible

Al momento de escribir código, es muy importante realizarlo en un estilo CLARO Y COHERENTE, para cuando vuelvas a leer dentro de unos días, dentro de unos años, sea más FÁCIL DE MANTENER Y MEJORAR y evitar que descifrar inconsistencias.

Por lo tanto Ud. debe realizar un esfuerzo adicional para hacer SU CÓDIGO TAN LEGIBLE COMO SEA POSIBLE.

	* Evite abreviar los nombres de variables
	* Documente sus clases y métodos
	* Refactorice sus líneas de código con funciones/métodos reutilizables

Por ejemplo, para una variable llamada balance_sheet_decrease, es mucho mas fácil interpretar en su mente que una variable abreviada bsd o bal_s_d. Si bien es cierto estas abreviaturas ahorran unos minutos al escribir, pero este ahorro se hace a expensas de horas o días de dudas ( ya que no se podrá entender cuando se vuelva a leer en el futuro). No vale la pena!

##1.2 PEP 8

1.Use 4 espacios para la identación.
	
	# alinear con el delimitador de apartura (paréntesis)
	foo = long_function_name(var_one, var_two,
							 var_three, var_four)

	# incluir mayor identación para distiguir del resto de código
	def long_function_name(
	        var_one, var_two, var_three, # tiene mayor identación
	        var_four): # tiene mayor identación
	    print(var_one) # tiene menor identación por ser el resto

	my_list = [
    	1, 2, 3,
    	4, 5, 6,
    	] #al inicio de la primer carácter de última línea
    #or

    my_list = [
    	1, 2, 3,
    	4, 5, 6,
    ] #al inicio
2.El límite de cada línea es de 79 carácteres

3.Separar 2 líneas a funciones y clases del nivel superior, separar por 1 línea a funciones

4.Los imports deben usarse en líneas separadas.
Deben tener el siguiente orden:

	primero: imports de las librerias estandares
	segundo: imports de terceros
	tercero: imports de tus aplicaciones

por ejemplo, para proyectos en django:

	# imports de librerías estandar
	from math import sqrt
	from os.path import abspath

	# imports del core de django
	from django.db import models
	from djang.utils.translation import ugetext_lazy as _

	# imports de aplicaciones de terceros
	from django_extensions.db.models import TimeStampedModel

	# imports de tus aplicaciones que creaste como parte del proyecto
	from splits.models import BananaSplit

##1.4 Usar explicit relative imports

Usar este tipo de imports, permitirá versatilidad al momento de cambiar el nombre de la app en el futuro, ya que al usar esto, no afectará en nada a los imports de la actual aplicación.

| Code                                 | Import Type       | Uso   |
| -------------------------------------|:-----------------:| -----:|
| from core.views import FoodView      | absolute import   | usar al importar desde fuera de la aplicación|
| from .models import WaffleCone       | explicit relative | usar cuando importas  de otro modulo de la aplicación actual|
| from cones.models import WaffleCOne  | implicit relative | usado frecuentemente para importar de otro modulo de la aplicación actual pero no es buena idea |

Adquiera el hábito de usar import relativos explicitos, es un buen hábito para cualquier programador Python.

##1.5 Evitar usar import *

Nunca usar:

	# ANTI-PATTERN: No hacer esto!
	from django.forms import *
	from django.db.models import *

Puede producir resultados impredecibles y algunas veces catastróficos.

Del ejemplo anterior, los formularios y modelos de Django tienen una clase llamada `CharField`, la clase de los modelos sobreescribiría al de formularios.

También hay que tener cuidado al import con los mismos nombres

	#ANTI-PATTERN: No hacer esto!
	from django.forms import CharField
	from django.db.models import CharField

##1.6 Guía de estilo de código Django

	- Use underscore, no camelCase, para variables, funciones y nombres de métodos.
	
	- Use InitialCaps para nombres de clases

	- Use {{ foo }}, no esto {{foo}}

	- fields names debe ser todo minusculas, using underscore en lugar de camelCase, `first_name`, no `FirstName`, no `First_Name`.

	- El orden en metodos debe ser como sigue:
		Todos los fields
		class Meta
		def __unicode__()
		def __str__()
		def save()
		def get_absolute_url()

##3.5 Usando una plantilla para generar tu propio Layout
	
	django-admin.py startproject --template=https://github.com/	twoscoops/django-twoscoops-project/zipball/master


##4.1 Regla de Oro del diseño de aplicaciones de Django

__Cada aplicación debe estar muy focalizada en hacer una tarea.__

>Si una aplicación no puede describir en una sola pabra su tarea y necesita de una o varias conjunciones (y), pues necesita ser particionada en otras más aplicaciones.

##4.2 Cómo nombrar sus apliciones

	- En lo posible mantener una sola palabra para el nombre.
	- Deben ser una version plural de su modelo principal, aunque hay varias buenas excepciones a esta regla, por ejemplo _blog_
	- Utilice nombres importables compatibles con PEP-8, nombres en minúsculas, sin números, puntos, espacios o caracteres especiales. Si es necesario para facilitar la lectura, se puede utilizar subguiones para separar las palabras, aunque no se recomienda esto.

##4.3 Ante la duda, mantener aplicaciones pequeñas

>Recuerde, es mejor tener muchas aplicaciones pequeñas que tener pocas aplicaciones gigantes.

No se preocupe demasiado en conseguir un diseño perfecto. 

A veces hay que volver a reescribirlos o separarlos, esto esta bien.

#5 Archivos Settings y Requirements

Algunas buenas prácticas que debemos seguir son:

* *Todos los archivos settings necesitan estar bajo el control de versiones*
* *No repetirse*: Debemos heredar de un archivo base en lugar de copiar y pegar el mismo contenido y tener pequeñas variaciones.
* *Mantener tus claves secretas seguras*: Ellas deben estar fuera del control de versiones

>The SECRET_KEY es usado para firmas criptograficas de django y necesita ser única. Al ser de conocimiento vulnera a muchas protecciones de seguridad de django.

>De la misma forma, los password de las base de datos, claves de AWS, OAuth tokens o cualquier otro datos sensible, necesitan mantenerse fuera del control de versiones.

#5.2 Usando multiples archivos settings

>Esta configuración descrita aqui esta basado en ["The best and worst of django"](https://speakerdeck.com/jacobian/the-best-and-worst-of-django) de Jacob Kaplan-Moss OSCON 2011

	settings/
		__init__.py
		base.py
		local.py
		staging.py
		production.py
		test.py

| Settings file   | Propósito |
| -------|-----:|
|base.py         | Configuraciones comunes de todas las instancias del proyecto|
|local.py        | Este archivo de configuración, usas cuando estas trabajando en tu proyecto localmente. Incluyes el modo DEBUG, herramientras como django-debug-toolbar. Algunas veces los desarrolladores lo llaman dev.py|
|staging.py      | La versión staging para correr un semi-privada versión de el sitio en un servidor de producción. Este es donde los managers y clientes deben observar antes que sea movido a producción |
|test.py         | Configuracion para correr pruebas incluyendo pruebas de ejecución, en memoria, en base de datos y de configuracion de logs|
|production.py   | Estes es el archivo usado en un(os) servidor(es) de produción. Algunas veces es llamado prod.py|

Para elegir algún modo de configuración, por ejemplo para correr el proyecto, sería de la siguiente manera:

	python manage.py runserver --settings=settings.local

#7 Funciones y Clases basadas en Vistas

##7.1 Cuándo usar FBVs or CBVs
Nosotros preferimos usar CBVs para la mayoria de casos, usando FBV solo en casos complicados que serían un dolor de cabeza con CBVs.

##7.2 Mantenga la lógica fuera de las URLs
Recuerde que django tiene una manera maravillosamente simple de definir rutas de URL. La simplicidad debe ser honrado y respetado. Las reglas y normas son obvias:

1. El módulo views deben contener la ĺógica.
2. El módulo URL debe contener las urls.

En síntesis, no hacer lo siguiente:

	urlpatterns = patterns("",
						   url(r"^something/$", 
						   	   DetailView.as_view(
						   	    	model=Tasting,
						   	    	template_name="tastings/detail.html"
						   		)
						   		)
						   	name="detail"
						   	)
#8 Mejores prácticas para Vistas Basadas en Clases

Con un poco de práctica, CBVs permitirán a los desarrolladores crear vistas a un ritmo asombroso.

>###Package tip: CBVs + django-braces son grandiosos juntos
Sentimos que django-braces es el componente que faltaba para CBVs de Django. Este provee un conjunto de mixin que hacen mucho mas facil y rápido implementar CBV.

Nosotros seguimos las siguientes directrices cuando escribrimos CBVs:

	* Menos código en tus vistas es mejor
	* Nunca repetir código en las vistas
	* Las vistas deben manejar la lógica de presentación. Trate de mantener la lógica del negocio en los modelos en cuanto sea posible.
	* Mantener tus vistas simples
	* Mantener tus mixin simples


##8.1 Usango Mixin con CBVs

Los mixin puede ser usados para agregar funcionalidad y comportamiento extra a tus clases.

Puede usar la potencia de mixin para componer una útil e interesante nueva vista de clase para tus aplicacion de Django.

Cuando usamos mixin para componer nuestas vistas en clases, recomendamos estas reglas de herencias provistas por _Kennet Love_:
	
1. Las clases basadas en vistas provistas por django, deben estar siempre a la derecha.

2. Los Mixin deben ir a la izquierda vista base.

3. Un Mixin debe siempre de heredar de un objeto de Python.  


Ejemplo de las reglas en acción:

	from django.views.generic import TemplateView

	
	class FreshFruitMixin(object):

		context = super(FreshFruitMixin, self).get_context_data(**kwargs)
		context["has_fresh_fuit"]=True

		return context

	class FruitFlavorView(FreshFruitMixin, TemplateView):
		template_name = "fruit_flavor.html"

En nuestro ejemplo, la clase `FruitFlavorView`, hereda de `FreshFruitMixin` y de `TemplateView`.

`TemplateView`, es una clase basada en vista de Django, este va a ir a la derecha(regla 1) y a la izquiera estarpa `FreshFruitMixin` (regla 2). De esta forma sabremos que nuestros metodos y propiedades se ejecutarán correctamente.

Finalmente, `FreshFruitMixin` hereda de `object` (regla 3).

...
...
...







#9. Patrones comunes para formularios

Combinando forms, models y view, permiten realizar un gran cantidad de trabajo con poco esfuerzo.

##9.2 Pattern 1: Simple ModelForm con Validadores por defecto
Usando `ModelsForms` con `CBV` para implementar add/edit forms puede ser con tan solo pocas lineas de código

	#flavors/views.py
	from django.views.generic import CreateView, UpdateView

	from braces.views import LoginRequiredMixin

	from .models import Sabor

	class SaborCreateView(LoginRequiredMixin, CreateView):
		model = Sabor

	class SaborUpdateView(LoginRequiredMixin, UpdateView):
		model = Sabor

Para resumir, como usa la validación por defecto:
	
	- SaborCreateView and FlavorUpdateView son asignado a Sabor como su modelo
	- Ambas vistas autogeran un ModelForm basado en el modelo Sabor
	- Estos ModelForms confian en las reglas de validación por defecto de los fields del model Sabor.

Si, Django te brinda muchas grandiosas validaciones de datos por defecto, pero en la práctica, los por defecto nunca son suficientes. Nosotros reconocemos esto, y en siguiente patron demostraremos como create un field validador personalizado.

##9.3 Pattern 2: Validadores pesonalizados en ModelForms

Lo que deseamos es estar seguros que cada `título field` de nuestro postre app, comience con la palabra `Tasty`?

Esta es un problema de validación de string, que puede ser resuelta con un simple *custom vield validator.*

En este patron, mostraremos como crear un custom single-field validators y demostrar como agregar luego a un modelo y formulario.

Imagine para el propositio de este ejemplo, que tenemos un proyecton con 2 diferentes modelos: un modelo Sabor para helado de sabadores y un modelo Batido para los diferentes tipos de batidos. Asumimos que ambos models tienen title fields.

Para validar todos los titulos del modelo, comenzamos creando un modulo _validators.py_

	#core/validators.py
	from django.core.exceptions import ValidationError

	def validate_tasty(value):
		"""
		Produce un ValidationError si
		el valor no inicia con la palabra
		'Tasty'
		"""
		if not value.startswith(u"Tasty"):
			msg = u"Debe iniciar con Tasty"
			raise ValidationError(msg)

...
...
...

##9.5 Pattern 4: Hacking Form Fields(2 CBV, 2 Forms, 1 Model)

Esta es donde iniciaremos con la forma fancy. Nosotros mostraremos una situación donde 2 views/forms corresponde a 1 modelo. Haremos un hacking a Django forms para producir un formulario con un comportamiento particular.

No es raro que los usuarios creen un registro que contingan algunos campos vacios para información adicional mas adelante. Un ejemplo podría ser una lista de tiendas, donde queremos que cada tienda entre al sistema lo más rápido posible, pero quiero agregar mas datos, como el número de teléfono y la descripción mas tarde. Aqui está nuestro modelo IceCreamStore:

	# stores/models.py
	from django.core.urlresolvers import reverse
	from django.db import models

	class IceCreamStore(models.Model):
		title = models.CharField(max_length=100)
		block_address = models.TextField()
		phone = models.CharField(max_length=20, blank=True)
		description = models.TextField(blank=True)

		def get_absolute_url(self):
			return reverse("store_detail", kwargs={"pk": self.pk})

El ModelForm por defecto para este model fuerza al usuario a ingresar los campos title y block_address, pero permite al usuario saltarse lso campos phone y description. Esto es genial para la entrada de datos inicial, pero como mencionamos antes, deseamos tener actualizaciones futuras de los datos para solicitar los campos phone y description.

La forma como implementabamos en el pasado era sobreescribir los campos phone y descripcion en un formulario y tener datos duplicados al del modelo, como el siguiente:

	# stores/forms.py
	from django import forms

	from .models import IceCreamStore

	
	class IceCreamStoreUpdateForm(forms.ModelForm):
		# No hacer esto! Duplicar el campo del modelo
		phone = forms.CharField(required=True)
		# No hacer esto! Duplicar el campo del modelo
		phone = forms.CharField(required=True)

		class Meta:
			models = IceCreanStore

El código anterior esta violando el principio **Don't Repeat Yourself**

Una mejor forma es aplicar los nuevos atricutos de cada campo en el método *__init__()* de ModelForm:

	# stores/forms.py
	# Lamando a phone y description de self.field dict-line object
	from django import forms

	from .models improt IceCreamStore


	class IceCreamStoreUpdateForm(forms.ModelForm):

		class Meta:
			model = IceCreamStore

		def __init__(self, *args, **kwargs):
			# llamar al metodo original __init__ antes de asignar
			# campos sobrecargados
			super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
			self.fields['phone'].required = True
			self.fields['description'].required = True

Esto permite no violar el principio DRY.


	# stores/forms.py
	from django import forms

	from .models import IceCreamStore


	class IceCreamStoreCreateForm(forms.ModelForm):

		class Meta:
			model = IceCreamStore
			fields = ("title", "block_address", )

	class IceCreamStoreUpdateForm(IceCreamStoreCreateForm):

		def __init__(self, *args, **kwargs):
			super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
			self.fields['phone'].required = True
			self.fields['description'].required = True

		class Meta(IceCreamStoreCreateForm.Meta)
			# show all the fields!
			fields = ("title", "block_address", "phone", "description", )

>Nunca usar ModelForms.Meta.exclude

Finalmente, ahora nosotros tenemos la necesidad de definir las correspondiente CBVs.

	# stores/views
	from django.views.generic import CreateView, UpdateView

	from .forms import IceCreamStoreCreateForm
	from .forms import IceCreamStoreUpdateForm
	from .models import IceCreamStore


	class IceCreamCreateView(CreateView):
		model = IceCreamStore
		form_class = IceCreamStoreCreateForm

	class IceCreamUpdateView(UpdateView):
		model = IceCreamStore
		form_class = IceCreamStoreUpdateForm

Ahora tenemos 2 vistas y 2 forms que trabaja con 1 modelo.

##9.6 Pattern 5: Reusable Search Mixin View

En este ejemplo, vamos a mostrar como reusar un formulario de búsqueda en 2 vistas correspondientes a 2 difentes modelos.

Asumimos que ambos modelos tienen un campo llamado _title_. Este ejemplo demostraremos como un solo CBV puede ser usado para proveer una simple funcionalidad para ambos modelos (Flavor y IceCreamStore).

Comenzaremos creando un simple search mmixin para nuestra vista.

	# core/views.py
	class TitleSearchMixin(object):

		def get_queryset(self):
			queryset = super(TitleSearchMixin, self).get_queryset()

			q = self.request.GET.get('q')

			if q:
				return queryset.filter(title__icontains=q)
			return queryset

Ahora, haremos que trabaje con las 2 vistas:

	# add to flavors/views.py
	from django.views.generic import ListView

	from core.views import TitleSearchMixin
	from .models import Flavor


	class FlavorListView(TitleSearchMixin, ListView):
		model = Flavor

	--------------------------------------------------
	# add to stores/views.py
	from django.views.generic import ListView

	from core.views import TitleSearchMixin
	from .models import Store


	class IcreCreamStoreListView(TitleSearchMixin, ListView):
		model = Store

Ahora tenemos el mismo mixin para ambas vistas. Los Mixin son una buena forma de reusar código, pero uasr muchos mixin hace complicado manter el código. Como siempre, debe mantener su código lo mas simple posible.

#10 More Things to Know About Forms

##10.1 Usar el método POST en formularios HTML

Cada formulario que altera datos, debe enviar sus datos via el método POST.

La única excepción que alguna vez notarás a la utilización del método POST en formularios, es son con los formularios de búsqueda, que normalmente presentar consultas que no dan lugar a ninguna alteración de los datos, éstos deben usar el método POST.

##10.1.1 No desactivar la protección CSRF de Django
Siempre usar la proteccion csrf con formularios que modifican datos.


