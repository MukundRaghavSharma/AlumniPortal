from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    # Sign-In #
    url(regex = r'^signin',
        view  = 'django.contrib.auth.views.login',
        name  = 'signin',
        kwargs = {'template_name' : 'Alumni/signin.html'}),

    # Sign-Up #
    url(regex = r'^signup',
        view  = 'Alumni.views.signup',
        name  = 'signup',),
    
    # Home Page #
    url(regex = r'^home',
        view = 'Alumni.views.home',
        name = 'home',),
    
    # Profile Page #
    url(regex = r'^profile/(?P<id>\d+)/$',
        view = 'Alumni.views.profile',
        name = 'Profile',),

    # Update the DB #
    url(regex = r'^update$',
        view = 'Alumni.views.update',
        name = 'testSave'),
    

    # Log out Page #
    url(regex = r'^logout', 
        view = 'Alumni.views.logout_user',
        name = 'Logout',),

    # Admin Page #
    url(regex = r'^admin/', 
        view = include(admin.site.urls)),

    # Signin Page 1#
    url(regex = r'^$', 
        view = 'Alumni.views.signin_1',
        name = 'signin_1',),

    # Class Page #
    url(regex = r'^class/(?P<classname>\w+)/$', 
        view = 'Alumni.views.class_view',
        name = 'class_view',),
)
'''
# Search Page #
# url(regex = r'^search$',
#    view = 'Alumni.views.search',
#    name = 'search'),
'''
