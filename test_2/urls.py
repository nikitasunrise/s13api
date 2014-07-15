from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'test_2.views.home', name='home'),

    url(r'^api/', include('api.urls')),
    url(r'^api/login/', include('api.urls')),
    url(r'^api/msg/', include('api.urls')),
    url(r'^api/id(?P<user_id>.+)/', 'api.views.msg'),
    url(r'^admin/', include(admin.site.urls)),
)
