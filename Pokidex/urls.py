from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Pokidex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index', name='index'),
    url(r'^dex/$', 'dex.views.index', name='index'),
    url(r'^search/(?P<search_string>\w{0,50})/$', 'dex.views.search', name='search'),
)
