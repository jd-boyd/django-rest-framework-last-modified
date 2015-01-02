from django.conf.urls import patterns, url

from tests.views import View2010, ViewUnwrapped


urlpatterns = patterns('',
                       (url(r'^/test_app/2010/$', View2010.as_view(), name='view2010')),
                       (url(r'^/test_app/unwrapped/$', ViewUnwrapped.as_view(), name='viewUnwrapped')),
                       )
