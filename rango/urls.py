from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'rango.views.index', name='index'),
                       url(r'^category/(?P<cat_name_slug>[\w\-]+)/$', 'rango.views.category', name='category'),
                       url(r'^add_category/$', 'rango.views.add_category', name='add_category'),
                       url(r'^add_page/(?P<cat_slug>[\w\-]+)/$', 'rango.views.add_page', name='add_page'),
                       url(r'^register/$', 'rango.views.register', name='register'),
                       url(r'^login/$', 'rango.views.user_login', name='login'),
                       url(r'^logout/$', 'rango.views.user_logout', name='logout'),
                       url(r'^about/$', 'rango.views.about', name="about"),
)
