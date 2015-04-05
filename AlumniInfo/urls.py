from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Alumni.urls')),
    url(r'^ajaximage/', include('ajaximage.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', 
        {'url': '/static/Alumni/images/favicon.ico'}),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    (r'^inplaceeditform/', include('inplaceeditform.urls')),
    
)
