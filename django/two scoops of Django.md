##1.1 La importancia de hacer tu código entendible

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

	- Use `underscore`, no camelCase, para mariales, funciones y nombres de métodos.
	
	- Use `InitialCaps` para nombres de clases

	- Use `{{ foo }}`, no esto {{foo}}

	- fields names debe ser todo minusculas, using underscore en lugar de camelCase, `first_name`, no `FirstName`, no `First_Name`.

	- El orden en metodos debe ser como sigue:
		Todos los fields
		class Meta
		def __unicode__()
		def __str__()
		def save()
		def get_absolute_url()

