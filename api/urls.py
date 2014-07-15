from django.conf.urls import *


urlpatterns = patterns('',
    url(r'^$', 'api.views.mainpage'),
    #url(r'^users/', 'api.views.users'),
    url(r'^msg/', 'api.views.history'),
    url(r'^id(?P<user_id>/.+)', 'api.views.msg')
)
