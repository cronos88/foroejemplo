from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', 'mundodjango.views.index', name='index'),
    url('^preguntas/(?P<pregunta_id>\d+)/$', 'mundodjango.views.pregunta_detalle', name='pregunta_detalle'),
    url('^preguntas/plus/(?P<pregunta_id>\d+)','mundodjango.views.plus_preg', name='plus_preg'),
    url('^preguntas/respuesta/plus/(?P<respuesta_id>\d+)','mundodjango.views.plus_resp', name='plus_resp'),
    url('^account/', include('allauth.urls')),
    url('^account/logout/', 'mundodjango.views.logout', name='logout'),
    url('^account/password/reset/', 'mundodjango.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)
