from django.conf.urls import patterns, include, url
from  rango.views import hello, about

urlpatterns = patterns('',


              url( r'^$', hello),
              url (r'^about', about)

)