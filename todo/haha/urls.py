from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import haha.views as vv
urlpatterns = patterns('',
      url(r'^hello/$',vv.hello,name = 'hello'),
      url(r'^search/', vv.search,name = 'search'),
      url(r'^todo/$',vv.todo_index,name = 'index'),
      url(r'^todo/add/$',vv.todo_add,name = 'todo_add'),
      url(r'^todo/data_add/$',vv.todo_adddata,name = 'add_data'),
      url(r'^todo/del',vv.todo_del,name = 'todo_del'),
      url(r'^todo/register$',vv.todo_reg,name = 'reg'),
    # Examples:
    # url(r'^$', 'haha.views.home', name='home'),
    # url(r'^haha/', include('haha.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
)
