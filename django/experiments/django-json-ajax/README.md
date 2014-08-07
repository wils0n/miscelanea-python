##consultas por ajax
Cuando consultas por ajax, tienes la ventaja de actualizar determinadas partes de la pagina **sin actualizarla**

Nuestro ejemplo:
Al hacer click en un titulo, mostrar la descripcion.  
Para esto capturas el id del articulo por la cual haces la consulta y envias el contenido mediante json, de esta manera mediante javascript ya puedes tratar esta informacioin; por cuestioenes practicas nosotros no hemos hecho interaccion con la bd, pero la idea es la misma.

	$(document).on('ready', main);

	//Al hacer click en 'a' del id 'clases' llamar a la funcion cargar_contenido_clase
	function main () {
		$('#clases').on('click', 'a', cargar_contenido_clase);
	}

	//capturas el id de la clase y consultas a la url 'cargar-contenido-clase/id'
	function cargar_contenido_clase (data) {
		var id = $(data.currentTarget).data('id');
		//alert(id)
		$.get('cargar-contenido-clase/' + id, cargar_clase)
	}

	//capturas el id, para identificar a que articulo desea el contenido
	url(r'^cargar-contenido-clase/(?P<id>\d+)$', 'app.views.cargar_contenido'),

	//aqui para validar que la consulta es por ajax, se puede agregar if request.is_ajax():
	//y envias el contenido y la descripcion (por agilidad enviamos directamente el contenido)
	return HttpResponse(
		json.dumps({'nombre': 'Hola Mundo', 'descripcion': 'print "Hola Mundo"'}), 
		content_type="application/json; charset=uft8"
		)

	//aqui capturo la data enviada por json y ya puedo trabajar con esa informacion a mi gusto
	function cargar_clase(data){
		var contenido = $('#contenido-clase');
		
		contenido.html('');

		$('<a class="regresar">').html('Regresar').appendTo(contenido);

		$('<h2>').html(data.nombre).appendTo(contenido);

		$('<p>').html(data.descripcion).appendTo(contenido);

	}