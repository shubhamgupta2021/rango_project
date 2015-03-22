from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rango_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',hello)
)
