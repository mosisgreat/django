from django.conf.urls import patterns, include, url
from sopenabi import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sopenabi.views.home', name='home'),
    url(r'^$', 'sndc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', "django.views.static.serve", {'document_root': settings.MEDIA_ROOT}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/js'}),
)
