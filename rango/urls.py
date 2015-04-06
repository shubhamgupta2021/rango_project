from django.conf.urls import patterns, include, url
from  rango.views import index, about, category, add_category, add_page, register, user_login, user_logout

urlpatterns = patterns('',


              url( r'^$', index),
              url (r'^about/$', about),
              url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name= "category"),
              url(r'^add_category/$', add_category),
              url(r'^(?P<category_name_slug>[\w\-]+)/add_page',add_page, name="add_page" ),
              url(r'^register/$', register, name= "register"),
              url(r'^login/$', user_login, name= "login"),
              url(r'^logout/$', user_logout, name = "logout")
)