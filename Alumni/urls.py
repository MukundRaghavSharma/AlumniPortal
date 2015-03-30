from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',

    # AUX Signin #
    url(regex = r'^signin/$',
        view  = 'django.contrib.auth.views.login',
        name  = 'signin',
        kwargs = {'template_name' : 'Alumni/signin.html'},),

    # AUX Signup #
    url(regex = r'^signup/$',
        view  = 'Alumni.views.signup',
        name  = 'signup',),
        
    # Sign-Up 1 - Launch Page #
    url(regex = r'^$',
        view  = 'Alumni.views.signup_1',
        name  = 'signup1',),

    # Sign-Up 2 - Basic Information #
    url(regex = r'^signup2/$',
        view  = 'Alumni.views.signup_2',
        name  = 'signup2',),

    # Sign-Up 3 - AKPsi Information #
    url(regex = r'^signup3/$',
        view  = 'Alumni.views.signup_3',
        name  = 'signup3',),

    # Sign-Up 4 - Career Information #
    url(regex = r'^signup4/$',
        view  = 'Alumni.views.signup_4',
        name  = 'signup4',),
   
    # Home Page #
    url(regex = r'^dashboard/$',
        view = 'Alumni.views.home',
        name = 'home',),
    
    # Profile Page #
    url(regex = r'^profile/(?P<brother_number>\d+)/$',
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

    # Class Page #
    url(regex = r'^class/(?P<classname>\w+)/$', 
        view = 'Alumni.views.class_view',
        name = 'class_view',),

    # Gallery Page #
    url(regex = r'^gallery/$', 
        view = 'Alumni.views.gallery_view',
        name = 'class_view',),
    
    # 404 Page #
    url(regex = r'^404$',
        view = 'Alumni.views.four_oh_four',
        name = '404',),

    # Donation Class #
    url(regex = r'^donations/$',
        view = 'Alumni.views.donations',
        name = 'donations',),

    # Family Tree Class #
    url(regex = r'^family_trees/$',
        view = 'Alumni.views.family_trees',
        name = 'family_trees',),

    # Search Functionality #
    url(regex = r'^search/$',
        view = 'Alumni.views.search',
        name = 'search',),

    # Send Emails #
    url(regex = r'^send_email/$',
        view = 'Alumni.views.send_email',
        name = 'search',),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
