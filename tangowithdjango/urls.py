from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tangowithdjango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^rango/', include('rango.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
