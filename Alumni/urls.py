from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(regex = r'^$',
        view  = 'django.contrib.auth.views.login',
        name  = 'signin',
        kwargs = {'template_name' : 'Alumni/signin.html'}),

    url(regex = r'^signup',
        view  = 'Alumni.views.signup',
        name  = 'signup',),

    url(regex = r'home',
        view = 'Alumni.views.home',
        name = 'home',),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^signin$', 'Alumni.views.signin'),
    #url(r'^signout$', 'Alumni.views.signout'),
)
