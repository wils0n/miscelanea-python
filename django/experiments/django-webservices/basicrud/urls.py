from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^nuevo/$', 'app.views.registrar', name='registrar'),
    #url(r'^editar/$', 'app.views.editar', name='editar'),
    url(r'^eliminar/(?P<id_usuario>\d+)$', 'app.views.eliminar', name='eliminar'),
    url(r'^editar/(?P<id_usuario>\d+)$', 'app.views.editar', name='editar'),
    url(r'^', include('webservices.wsUsuarios.urls')),

    url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), #para servir imagenes
    # url(r'^basicrud/', include('basicrud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
