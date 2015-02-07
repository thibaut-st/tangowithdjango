from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'rango.views.index', name='index'),
)
