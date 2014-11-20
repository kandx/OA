from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'account/login.html'},name='login'),
)
