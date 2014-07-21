from django.conf.urls import patterns, include, url
from main.views import IndexView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'main.views.IndexView'),
    url(r'^$', IndexView.as_view()),
    url(r'^gen/', 'main.views.generate'),
    # url(r'^righttime/', include('righttime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
