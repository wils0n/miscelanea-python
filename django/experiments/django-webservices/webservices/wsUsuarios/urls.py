from django.conf.urls import patterns, include, url


urlpatterns = patterns('webservices.wsUsuarios.views',
    # Examples:
    url(r'^ws/usuarios/$', 'wsUsuarios_view', name='webservices_Usuario'),
)