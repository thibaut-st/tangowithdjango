from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'rango.views.index', name='index'),
                       url(r'^about/$', 'rango.views.about', name="about"),
)
