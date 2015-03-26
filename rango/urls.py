from django.conf.urls import patterns, include, url
from  rango.views import index, about

urlpatterns = patterns('',


              url( r'^$', index),
              url (r'^about', about)

)