from django.conf.urls import patterns, include, url
from django.contrib import admin

from tangowithdjango import settings


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tangowithdjango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^rango/', include('rango.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )