from django.conf.urls import patterns, include, url
from django.contrib import admin
#from userprofiles.views import LoginView
from userprofiles.views import ListView, DetailView, DeleteView, UpdateView, CreateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^New/', CreateView.as_view(), name='create'),
    url(r'^detail(?P<pk>\d+)$',DetailView.as_view(),name='detail'),
    url(r'^list/$',ListView.as_view(),name='list'),
    url(r'^update(?P<pk>\d+)$',UpdateView.as_view(),name='update'),
    url(r'^delete(?P<pk>\d+)$',DeleteView.as_view(),name='delete'),
    url(r'^$','userprofiles.views.listar'),
    #url(r'^logout$', 'app.views.cerrar'),
)
