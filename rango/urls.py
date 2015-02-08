from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'rango.views.index', name='index'),
                       url(r'^category/(?P<cat_name_slug>[\w\-]+)/$', 'rango.views.category', name='category'),
                       url(r'^about/$', 'rango.views.about', name="about"),
)
